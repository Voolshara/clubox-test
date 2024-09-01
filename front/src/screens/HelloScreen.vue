<template>
  <div
    class="h-screen w-full pt-14 flex flex-col items-center justify-center gap-y-14 bg-gradient-to-br from-violet-900 to-pink-900"
  >
    <span class="text-3xl font-bold">Введи свою дату рождения</span>
    <CalendarSlider />

    <button class="w-5/6 bg-white text-black py-3 rounded-2xl">
      Продолжить
    </button>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent } from "vue";
import CalendarSlider from "../components/CalendarSlider/CalendarSlider.vue";
import { useSelectedDateStore } from "../store";

// interface TelegrammedWindow extends Window {
//   Telegram: any;
// }

export default defineComponent({
  components: { CalendarSlider },
  setup() {
    const store = useSelectedDateStore();
    const selectedDate = computed(() => store.getSelectedDate);
    // const { id, first_name, last_name, username } = (
    //   window as unknown as TelegrammedWindow
    // ).Telegram.WebApp.initDataUnsafe.user;

    // return { id, first_name, last_name, username };
    return { selectedDate };
  },
});
</script>
