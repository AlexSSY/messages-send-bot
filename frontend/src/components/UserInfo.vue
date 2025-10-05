<template>
  <h3 class="text-xl font-semibold mb-4">User Info</h3>
  <div class="tg-card rounded-xl p-4">
    <div class="flex items-center mb-4">
      <div class="w-12 h-12 bg-blue-500 rounded-full flex items-center justify-center text-white font-bold mr-3">
        <span id="userInitials">{{ userInitials }}</span>
      </div>
      <div>
        <h4 id="userName" class="font-medium">{{ userName }}</h4>
        <p id="userUsername" class="tg-text-hint text-sm">@{{ userUsername }}</p>
      </div>
    </div>
    <div class="grid grid-cols-2 gap-4 text-center">
      <div>
        <p class="font-medium" id="userId">{{ userId }}</p>
        <p class="tg-text-hint text-sm">User ID</p>
      </div>
      <div>
        <p class="font-medium" id="userLanguage">{{ userLanguage }}</p>
        <p class="tg-text-hint text-sm">Language</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userInitials: "U",
      userName: "User Name",
      userUsername: "@username",
      userId: "ID",
      userLanguage: "EN"
    }
  },
  mounted() {
    if (tg.initDataUnsafe && tg.initDataUnsafe.user) {
      const user = tg.initDataUnsafe.user;
      this.userInitials = user.first_name ? user.first_name.charAt(0).toUpperCase() : 'U';
      this.userName = user.first_name || 'User';
      this.userUsername = user.username ? `@${user.username}` : 'No username';
      this.userId = user.id;
      this.userLanguage = user.language_code ? user.language_code.toUpperCase() : 'EN';
    }
  }
}
</script>