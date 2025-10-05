<script setup>
import { onMounted } from 'vue'
import { 
    initAccordions, 
    initCarousels, 
    initCollapses, 
    initDials, 
    initDismisses, 
    initDrawers, 
    initDropdowns, 
    initModals, 
    initPopovers, 
    initTabs, 
    initTooltips } from 'flowbite'
import HeaderComponent from './components/HeaderComponent.vue';

// initialize components based on data attribute selectors
onMounted(() => {
    initAccordions();
    initCarousels();
    initCollapses();
    initDials();
    initDismisses();
    initDrawers();
    initDropdowns();
    initModals();
    initPopovers();
    initTabs();
    initTooltips();
});
</script>

<template>
  <!-- <HeaderComponent /> -->

  <!-- Main Content -->
  <main class="pt-8 pb-20 safe-area-top safe-area-bottom">
    <div class="container mx-auto px-4">
      <router-view />
    </div>
  </main>
</template>

<script>
export default {
  componensts: [
  ]
}
</script>