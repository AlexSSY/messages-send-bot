<template>
  <h3 class="text-xl font-semibold mb-4">Features</h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="tg-card rounded-xl p-4">
      <div class="flex items-center mb-2">
        <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center mr-3">
          <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z">
            </path>
          </svg>
        </div>
        <h4 class="font-medium">Secure</h4>
      </div>
      <p class="tg-text-hint text-sm">Your data is protected with end-to-end encryption</p>
    </div>

    <div class="tg-card rounded-xl p-4">
      <div class="flex items-center mb-2">
        <div class="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center mr-3">
          <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z">
            </path>
          </svg>
        </div>
        <h4 class="font-medium">Fast</h4>
      </div>
      <p class="tg-text-hint text-sm">Lightning fast performance with optimized components</p>
    </div>
  </div>
</template>