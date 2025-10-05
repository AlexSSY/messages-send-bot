<template>
  <header class="tg-header fixed top-0 left-0 right-0 z-50 safe-area-top">
    <nav class="px-4 py-3 flex justify-between items-center">
      <button id="backButton" @click.stop="backClick" class="p-2 rounded-lg hover:bg-gray-100 transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
        </svg>
      </button>
      <h1 class="text-lg font-medium">Telegram Web App</h1>
      <button @click.stop="menuClick" id="menuButton" class="p-2 rounded-lg hover:bg-gray-100 transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
      </button>
    </nav>
  </header>
</template>

<script>
export default {
  methods: {
    backClick() {
      tg.BackButton.isVisible ? tg.BackButton.onClick() : history.back();
    },
    menuClick() {
      tg.showPopup({
        title: 'Menu',
        message: 'This is a menu popup',
        buttons: [
          { id: 'settings', type: 'default', text: 'Settings' },
          { id: 'help', type: 'default', text: 'Help' },
          { type: 'cancel' }
        ]
      }, function (buttonId) {
        if (buttonId === 'settings') {
          tg.showAlert('Settings clicked');
        } else if (buttonId === 'help') {
          tg.showAlert('Help clicked');
        }
      });
    }
  }
}
</script>