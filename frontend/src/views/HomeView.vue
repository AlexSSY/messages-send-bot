<template>
  <!-- Hero Section -->
  <section class="mb-8">
    <HeroComponent />
  </section>

  <!-- Features Section -->
  <section class="mb-8">
    <FeaturesComponent />
  </section>

  <!-- Action Section -->
  <section class="mb-8">
    <ActionsComponent />
  </section>

  <!-- User Info Section -->
  <section class="mb-8">
    <UserInfo />
  </section>
</template>

<script>
import ActionsComponent from '@/components/ActionsComponent.vue';
import FeaturesComponent from '@/components/FeaturesComponent.vue';
import HeroComponent from '../components/HeroComponent.vue';
import UserInfo from '@/components/UserInfo.vue';

export default {
  name: "HomeView",
  components: {
    ActionsComponent,
    FeaturesComponent,
    HeroComponent,
    UserInfo
  },
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