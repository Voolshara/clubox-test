<template>
  <div
    class="h-screen w-full pt-14 flex flex-col items-center justify-center gap-y-14 bg-gradient-to-br from-violet-900 to-pink-900"
  >
    <span class="text-3xl font-bold"
      >Введи свою дату рождения
      {{ JSON.stringify(first_name, last_name, username) + "" }}</span
    >
    <CalendarSlider />

    <button class="w-5/6 bg-white text-black py-3 rounded-2xl">
      Продолжить
    </button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import CalendarSlider from "../components/CalendarSlider/CalendarSlider.vue";

interface TelegrammedWindow extends Window {
  Telegram: any;
}

export default defineComponent({
  components: { CalendarSlider },
  setup() {
    const { first_name, last_name, username } = (
      window as unknown as TelegrammedWindow
    ).Telegram.WebApp.initDataUnsafe.user;

    return { first_name, last_name, username };
  },
});
</script>
