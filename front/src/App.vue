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

export default {
  components: { NavBar, HelloScreen, BirthScreen },
  setup() {
    const store = useUserDataStore();
    const userData = computed(() => store.getUserData);
    getUserData("111");
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
