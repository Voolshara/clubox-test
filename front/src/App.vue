<template>
  <div class="bg-black text-white flex flex-col w-screen h-screen">
    <LK />
  </div>
</template>

<script lang="ts">
// import { computed } from "vue";
// import NavBar from "./components/NavBar.vue";
// import Swiper from "./components/Swiper/Swiper.vue";
import LK from "./screens/LK.vue";
// import HelloScreen from "./screens/HelloScreen.vue";
// import BirthScreen from "./screens/BirthScreen.vue";
// import { useUserDataStore } from "./store/";
// import { getUserData } from "./api/";
// import { TelegrammedWindow } from "./types/telegrammedWindow.types.ts";

export default {
  // components: { NavBar, HelloScreen, BirthScreen },
  components: { LK },
  setup() {
    // const store = useUserDataStore();
    // const userData = computed(() => store.getUserData);
    // const { id } = (window as unknown as TelegrammedWindow).Telegram.WebApp
    //   .initDataUnsafe.user;
    // const start_param = (window as unknown as TelegrammedWindow).Telegram.WebApp
    //   .initDataUnsafe.start_param;
    // if (start_param !== undefined) {
    //   const splittedInitData = (start_param as string).split("tg_user-")[1];
    //   const tg_id = splittedInitData.split("&")[0];
    //   getUserData(tg_id);
    // } else {
    //   getUserData(id);
    // }
    // return { userData };
  },
};
</script>
