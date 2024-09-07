<template>
  <div
    class="relative z-10 w-screen h-screen bg-lk-bg bg-cover text-white flex flex-col gap-y-5 items-center justify-between"
  >
    <div class="w-full h-16 bg-black"></div>
    <div class="w-5/6 h-full flex flex-col items-center gap-y-5">
      <ButtonLK
        :button-is-gradient="false"
        :button-label="'Редактировать профиль'"
        @button-callback="editLKButton"
      />
      <ProfileInfo />
    </div>
    <div class="w-full h-20 bg-black"></div>
  </div>
</template>

<script setup lang="ts">
import ButtonLK from "../components/ButtonLK/ButtonLK.vue";
import { IconsEnum } from "../types/Button.types";
import ProfileInfo from "../components/ProfileInfo/ProfileInfo.vue";

const editLKButton = () => alert("editLKButton");
</script>
