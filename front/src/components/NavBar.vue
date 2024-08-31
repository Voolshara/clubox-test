<template>
  <nav
    class="absolute w-full h-14 bg-black flex flex-row justify-between items-center"
  >
    <div class="w-14 h-14 flex items-center justify-center">
      <div class="w-8 h-8">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          strokeWidth="{2}"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            d="M15.75 19.5 8.25 12l7.5-7.5"
          />
        </svg>
      </div>
    </div>

    <div class="flex flex-col">
      <span class="text-lg"> Клубные боты </span>
      <span class="text-gray-700"> боты </span>
    </div>

    <div class="w-14 h-14 flex items-center justify-center">
      <div class="w-8 h-8 bg-white rounded-full"></div>
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  setup() {},
});
</script>
