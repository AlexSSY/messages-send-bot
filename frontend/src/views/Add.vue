<template>
  <div>
    <h1>👤 Phone</h1>
    <router-link to="/">Back Home</router-link>
    <input type="text" v-model="phone_number" placeholder="phone">
    <button @click.stop="send">Send</button>
  </div>
</template>

<script>
import { checkPhone, addPhone } from "../services"

export default {
  data() {
    return {
      phone_number: ""
    }
  },
  methods: {
    async send() {
      var auth_status = await checkPhone(this.phone_number)

      if (auth_status === "phone") {
        auth_status = await addPhone(this.phone_number)
        if (auth_status === "code") {
          this.$router.push({ name: "Code", params: { phoneNumber: this.phone_number } });
        }
      } else if (auth_status === "code") {
        this.$router.push({ name: "Code", params: { phoneNumber: this.phone_number } });
      }
    }
  }
}
</script>
