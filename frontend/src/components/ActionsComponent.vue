<template>
  <h3 class="text-xl font-semibold mb-4">Actions</h3>
  <div class="space-y-3">
    <button @click.stop="primaryClick" class="tg-button w-full py-3 rounded-xl font-medium transition-all transform active:scale-95">
      Primary Action
    </button>
    <button class="w-full py-3 border border-gray-300 rounded-xl font-medium transition-colors hover:bg-gray-50">
      Secondary Action
    </button>
  </div>
</template>

<script>
export default {
  name: "ActionsComponent",
  methods: {
    primaryClick() {
      this.$router.push({ name: "Add"})
    }
  }
}
</script>