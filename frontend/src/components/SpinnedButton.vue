<template>
  <button @click="$emit('click', $event)"
    class="tg-button w-full py-3 rounded-xl font-medium transition-all transform active:scale-95">
    <span v-if="!isLoading">Send</span>
    <svg v-else id="spinner" class="animate-spin h-5 w-5 text-white mx-auto" xmlns="http://www.w3.org/2000/svg"
      fill="none" viewBox="0 0 24 24">
      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"></path>
    </svg>
  </button>
</template>

<script>
export default {
  name: "SpinnedButton",
  props: {
    isLoading: {
      default: false
    }
  },
  emits: ['click']
}
</script>