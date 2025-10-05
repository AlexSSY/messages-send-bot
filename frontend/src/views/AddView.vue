<template>
  <div class="max-w-md mx-auto">

    <div class="relative z-0 w-full mb-5 group">
      <PhoneInput :disabled="form.step !== 'phone' && form.phone.length > 0" label="Phone" v-model="phone"/>
    </div>

    <div v-if="form.step === 'code' || form.code.length > 0" class="relative z-0 w-full mb-5 group">
      <PhoneInput :disabled="form.step !== 'code' && form.code.length > 0" label="Code" v-model="code"/>
    </div>

    <div v-if="form.step === 'password' || form.password.length > 0" class="relative z-0 w-full mb-5 group">
      <PhoneInput :disabled="form.step !== 'password' && form.password.length > 0" label="Password" v-model="password"/>
    </div>

    <SpinnedButton :is-loading="isLoading" @click.stop="doSend" />

  </div>
</template>

<script>
import PhoneInput from '../components/PhoneInput.vue';
import SpinnedButton from '../components/SpinnedButton.vue';

import { sendCodeRequest, verifyCode, signInWith2fa } from '../services';


function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

export default {
  components: {
    PhoneInput,
    SpinnedButton
  },
  data() {
    return {
      form: {
        phone: '',
        code: '',
        password: '',
        loading: false,
        step: 'phone',
        phone_code_hash: '',
        errors: {}
      },
      phone: "",
      isLoading: false
    }
  },
  methods: {
    async _sendCodeRequest() {
      this.isLoading = true;
      var result = await sendCodeRequest(this.phone)
      
      if (result.success) {
        this.form.phone_code_hash = result.data.phone_code_hash
        this.form.phone = this.phone
        this.form.step = "code"
      }

      this.isLoading = false;
    },
    async _verifyCode() {
      this.isLoading = true;
      var result = await verifyCode(this.code, this.form.phone, this.form.phone_code_hash)
      
      if (result.success) {
        this.form.step = "done"
        alert("Authenticated!")
        this.$router.push('/')
      }

      this.isLoading = false;
    },
    async _signInWith2fa() {
      this.isLoading = true;
      var result = await signInWith2fa(this.form.code, this.form.phone, this.form.phone_code_hash)

      if (result.success) {
        this.form.step = "done"
        alert("Authenticated!")
        this.$router.push('/')
      }

      this.isLoading = false;
    },
    async doSend() {
      if (this.isLoading) {
        return;
      }

      switch (this.form.step) {
        case "phone":
          await this._sendCodeRequest()
          break;
        case "code":
          await this._verifyCode()
          break;
        case "password":
          await this._signInWith2fa()
          break;
        default:
          break;
      }
    }
  }
}
</script>
