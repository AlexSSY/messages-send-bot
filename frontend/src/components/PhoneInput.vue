<template>
  <input 
    :id="id" 
    type="text"
    :name="id"
    :value="modelValue" 
    @input="$emit('update:modelValue', $event.target.value)"
    :disabled="disabled" 
    class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" 
    placeholder=" " />
    <label :for="id" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 
      duration-300 transform -translate-y-3 scale-90 top-3 -z-10 origin-[0] peer-focus:start-0 
      rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-blue-600 peer-focus:dark:text-blue-500 
      peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-90 peer-focus:-translate-y-3">
      {{ label }}
    </label>
</template>

<script>
export default {
  name: "PhoneInput",
  props: {
    modelValue: {
      type: String,
      default: ''
    },
    label: {
      type: String,
      required: true
    },
    disabled: {
      type: Boolean,
      default: false
    },
    error: {
      type: String,
      default: ''
    },
  },
  emits: ['update:modelValue'],
  computed: {
    id() {
      return `input-${this.label.toLowerCase().replace(/\s+/g, '-')}`
    },
    classList() {
      return [
        'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer',
        this.error ? 'error-field' : '',
        this.disabled ? 'bg-gray-100 opacity-70' : ''
      ]
    }
  },
}
</script>