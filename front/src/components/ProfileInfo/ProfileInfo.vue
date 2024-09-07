<template>
  <div class="relative w-full border rounded-3xl border-gray-700">
    <div class="w-full h-full absolute bg-black opacity-25 rounded-3xl"></div>

    <div class="flex flex-row gap-x-5 relative z-10 my-2 mx-4">
      <div class="w-1/3 bg-purple-900 rounded-xl">
        <Icon :icon="IconsEnum.userIcon" />
      </div>

      <div class="h-24 flex flex-col gap-y-4 justify-center">
        <div class="flex flex-row gap-x-1 items-end">
          <Icon :icon="IconsEnum.userIcon" class="h-4" />
          <span class="text-2xl-pure font-bold">Евгений</span>
        </div>

        <div class="flex flex-row gap-x-3">
          <div class="w-[30px] h-[30px] bg-white"></div>
          <div class="flex flex-col text-base-pure text-gray-400">
            <span>Посетил клуб</span>
            <span>3 раза</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Icon from "../ButtonLK/Icon.vue";
import { IconsEnum } from "../../types/Button.types";
</script>
