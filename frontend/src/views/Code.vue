<script setup>
defineProps(["phoneNumber"])
</script>

<template>
  <div>
    <h1>👤 Code</h1>
    <router-link to="/">Back Home</router-link>
    <input type="text" v-model="code" placeholder="code">
    <button @click.stop="send">Send</button>
  </div>
</template>

<script>
import { checkCode } from '../services';

export default {
  data() {
    return {
      code: ""
    }
  },
  methods: {
    async send() {
      var auth_status = await checkCode(this.code, this.phoneNumber)

      if (auth_status === "authorized") {
        alert("Authorized!")
      }
    }
  }
}
</script>
