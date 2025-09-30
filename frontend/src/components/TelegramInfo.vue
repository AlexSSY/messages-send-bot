<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">Telegram Debug Info</h1>

    <div v-if="queryParams">
      <h2 class="text-xl font-semibold mb-2">Query Params</h2>
      <pre class="bg-gray-100 p-2 rounded">{{ queryParams }}</pre>
    </div>

    <div v-if="tgData">
      <h2 class="text-xl font-semibold mt-4 mb-2">Telegram WebApp Data</h2>
      <pre class="bg-gray-100 p-2 rounded">{{ tgData }}</pre>
    </div>

    <div v-if="!queryParams && !tgData" class="text-gray-500">
      No Telegram data found
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"

const queryParams = ref(null)
const tgData = ref(null)

onMounted(() => {
  // Получаем данные из URL (start=payload и др.)
  const params = Object.fromEntries(new URLSearchParams(window.location.search))
  if (Object.keys(params).length) {
    queryParams.value = params
  }

  // Проверяем Telegram WebApp объект
  if (window.Telegram?.WebApp) {
    const tg = window.Telegram.WebApp
    // Сохраняем всё доступное
    tgData.value = {
      initData: tg.initData,                  // HMAC-строка
      initDataUnsafe: tg.initDataUnsafe,      // разобранные данные (user, chat, query_id и др.)
      themeParams: tg.themeParams,            // цвета интерфейса Telegram
      version: tg.version,
      isExpanded: tg.isExpanded
    }
  }
})
</script>

<style scoped>
pre {
  overflow-x: auto;
}
</style>
