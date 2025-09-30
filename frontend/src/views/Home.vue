<script setup>
</script>

<template>
  <div>
    <h1>🏠 Home</h1>
    <button @click="sessions">Sessions</button>
  </div>
</template>

<script>
export default {
  methods: {
    get_me: async () => {
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
    sessions: async () => {
       await fetch("/api/sessions", {
        headers: {
          "X-Telegram-Init-Data": window.Telegram.WebApp.initData,
        },
      })
      .then(response => response.json())
      .then(jsonData => {
        alert(JSON.stringify(jsonData))
      })
    }
  }
}
</script>