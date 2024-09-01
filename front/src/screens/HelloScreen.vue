<template>
  <div
    v-if="is_clicked"
    class="h-screen w-full pt-14 flex flex-col items-center justify-center gap-y-14 bg-gradient-to-br from-violet-900 to-pink-900"
  >
    Loading ...
  </div>
  <div
    v-else
    class="h-screen w-full pt-14 flex flex-col items-center justify-center gap-y-14 bg-gradient-to-br from-violet-900 to-pink-900"
  >
    <span class="text-3xl font-bold">Введи свою дату рождения</span>
    <CalendarSlider />

    <button
      class="w-5/6 bg-white text-black py-3 rounded-2xl"
      v-on:click="sendUserData"
    >
      Продолжить
    </button>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent } from "vue";
import CalendarSlider from "../components/CalendarSlider/CalendarSlider.vue";
import { useSelectedDateStore } from "../store";
import { setUserData } from "../api";
import { TelegrammedWindow } from "../types/telegrammedWindow.types.ts";

export default defineComponent({
  components: { CalendarSlider },
  setup() {
    let is_clicked = false;
    const store = useSelectedDateStore();
    const selectedDate = computed(() => store.getSelectedDate);
    const { id, first_name, last_name, username } = (
      window as unknown as TelegrammedWindow
    ).Telegram.WebApp.initDataUnsafe.user;

    const sendUserData = () => {
      setUserData({
        date_birth: selectedDate.value,
        tg_id: id,
        tg_lastname: last_name,
        tg_name: first_name,
        tg_username: username,
      });
    };

    return { sendUserData, is_clicked };
  },
});
</script>
