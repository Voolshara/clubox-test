<template>
  <div
    class="h-screen w-full pt-14 flex flex-col gap-y-10 justify-center items-center bg-gradient-to-br from-violet-900 to-pink-900"
  >
    <div class="w-5/6 flex flex-col items-start gap-y-5">
      <p>Имя пользователя: {{ props.userData?.tg_name }}</p>
      <p>Фамилия пользователя : {{ props.userData?.tg_lastname }}</p>
      <p>Юзернейм пользователя: {{ props.userData?.tg_username }}</p>
      <div class="flex flex-col gap-y-3">
        <p>До дня рождения:</p>
        <p>Дней: {{ props.userData.birth_data.days_for_birth }}</p>
        <p>Часов: {{ props.userData.birth_data.hours_for_birth }}</p>
        <p>Минут: {{ props.userData.birth_data.minutes_for_birth }}</p>
      </div>
    </div>
    <button
      class="w-5/6 bg-white text-black py-3 rounded-2xl"
      v-on:click="clickShare"
    >
      Поделиться
    </button>
  </div>
</template>

<script lang="ts" setup>
import { defineProps } from "vue";
import { UserDataType } from "../types/user.types.ts";
import { TelegrammedWindow } from "../types/telegrammedWindow.types.ts";

const props = defineProps({
  userData: { type: Object as () => UserDataType, required: true },
});

const clickShare = () => {
  const { id } = (window as unknown as TelegrammedWindow).Telegram.WebApp
    .initDataUnsafe.user;

  navigator.share({
    text: `https://t.me/spspspspspspspmchbot?startapp=tg_user-${id}`,
  });
};
</script>
