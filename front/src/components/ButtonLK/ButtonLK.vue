<template>
  <button
    :class="`text-sm cursor-pointer w-fit px-6 py-1 flex flex-row gap-x-2 rounded-3xl ${
      props.buttonIsGradient
        ? 'bg-purple-600 text-white'
        : 'bg-white text-black'
    }`"
    @click="emit('buttonCallback')"
  >
    <div className="w-6 h-6" v-if="buttonIcon !== undefined">
      <Icon :icon="buttonIcon" />
    </div>
    {{ props.buttonLabel }}
  </button>
</template>

<script setup lang="ts">
import { PropType } from "vue";
import Icon from "./Icon.vue";
import { IconsEnum } from "../../types/Button.types";

const props = defineProps({
  buttonLabel: String,
  buttonIcon: String as PropType<IconsEnum>,
  buttonIsGradient: Boolean,
});

const emit = defineEmits<{
  (e: "buttonCallback"): void;
}>();
</script>
