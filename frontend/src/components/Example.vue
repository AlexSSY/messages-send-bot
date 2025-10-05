<template>
  <div class="relative z-0 w-full mb-6 group">
    <input type="text" id="username"
      :class="inputClasses"
      placeholder=" " required />
    <label for="username" :class="labelClasses">
      Username
    </label>
  </div>
</template>

<script>
export default {
  name: "Example",
  computed: {
    inputClasses() {
      return "peer block w-full appearance-none border-0 border-b-2 border-gray-300 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
    },
    labelClasses() {
      return `absolute top-3 -z-10 origin-[0] scale-100 transform text-gray-500 duration-300 
           peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 
           peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600`
    }
  }
}
</script>