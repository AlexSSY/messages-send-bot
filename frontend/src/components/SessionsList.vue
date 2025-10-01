<template>
<div v-if="sessions.length == 0"><router-link to="/add">add</router-link></div>
<div v-if="sessions.length != 0">
  <ul>
    <li v-for="(value, idx) in sessions" :id="idx">{{ value }}</li>
  </ul>
</div>
</template>

<script>
export default {
  data: () => {
    return {
      sessions: []
    }
  },
  async mounted() {
    await this.get_sessions()
  },
  methods: {
    async get_sessions() {
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