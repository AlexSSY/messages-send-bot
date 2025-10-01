<script setup>
import SessionsList from '../components/SessionsList.vue';
</script>

<template>
  <div>
    <h1>🏠 Home</h1>
    <button @click="get_me">me</button>
    <sessions-list />
  </div>
</template>

<script>
export default {
  data: () => {
    return {}
  },
  methods: {
    async get_me() {
      await fetch("/api/me", {
        headers: {
          "X-Telegram-Init-Data": window.Telegram.WebApp.initData,
        },
      })
      .then(response => response.json())
      .then(jsonData => {
        alert(JSON.stringify(jsonData))
      })
    },
  }
}
</script>