<template>
  <span class="" :class="{ 'font-bold': isSelected }">{{ props.label }}</span>
</template>

<script lang="ts" setup>
import { defineProps } from "vue";

const props = defineProps({
  label: { type: String, required: true },
  isSelected: { type: Boolean, required: true },
});
</script>
