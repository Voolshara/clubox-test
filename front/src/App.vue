<template>
  <div class="text-white flex flex-col">
    <NavBar />
    <HelloScreen v-if="!userData" />
    <BirthScreen v-else :userData="userData" />
  </div>
</template>

<script lang="ts">
import { computed } from "vue";
import NavBar from "./components/NavBar.vue";
import HelloScreen from "./screens/HelloScreen.vue";
import BirthScreen from "./screens/BirthScreen.vue";
import { useUserDataStore } from "./store/";
import { getUserData } from "./api/";
import { TelegrammedWindow } from "./types/telegrammedWindow.types.ts";

export default {
  components: { NavBar, HelloScreen, BirthScreen },
  setup() {
    const store = useUserDataStore();
    const userData = computed(() => store.getUserData);

    const initData = (window as unknown as TelegrammedWindow).Telegram.WebApp
      .initData;

    if (initData) {
      alert((initData as string).split("tg_user-")[1]);
      const tg_id = (initData as string).split("tg_user-")[1].split("&")[0];
      alert(tg_id);
      getUserData(tg_id);
    } else {
      const { id } = (window as unknown as TelegrammedWindow).Telegram.WebApp
        .initDataUnsafe.user;
      getUserData(id);
    }
    return { userData };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
