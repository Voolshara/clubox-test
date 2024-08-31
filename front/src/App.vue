<template>
  <div class="text-white flex flex-col">
    <NavBar />
    <HelloScreen />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import NavBar from "./components/NavBar.vue";
import HelloScreen from "./screens/HelloScreen.vue";

@Options({
  components: {
    NavBar,
    HelloScreen,
  },
})
export default class App extends Vue {}
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
