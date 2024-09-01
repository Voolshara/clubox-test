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

    const { id } = (window as unknown as TelegrammedWindow).Telegram.WebApp
      .initDataUnsafe.user;

    const initData = (window as unknown as TelegrammedWindow).Telegram.WebApp
      .initData;

    const splittedInitData = (initData as string).split("tg_user-")[1];

    if (splittedInitData) {
      const tg_id = splittedInitData.split("&")[0];
      getUserData(tg_id);
    } else {
      alert("work");
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
