<template>
  <div class="w-full h-full flex flex-col items-center gap-y-6">
    <SwiperComponent
      class="w-full h-fit"
      :slides-per-view="1.1"
      :space-between="-16"
      @swiper="onSwiper"
      @slideChange="onSlideChange"
    >
      <swiper-slide v-for="(event, index) in EventsData" :key="index">
        <div :class="`mx-4 ${index !== nowSwiperIndex ? 'p-2' : ''}`">
          <img :src="event.event_photo" alt="" />
        </div>
      </swiper-slide>
    </SwiperComponent>

    <div class="flex flex-col gap-y-6 w-5/6">
      <div class="relative -left-4 flex flex-col gap-y-2 w-full">
        <div class="flex flex-row items-center gap-x-3">
          <i class="rounded-full bg-[#8d60d7] p-1 h-fit"></i>
          <span class="font-bold text-3xl">{{
            EventsData[nowSwiperIndex].event_title
          }}</span>
        </div>
        <span class="text-gray-400 ml-5">{{
          EventsData[nowSwiperIndex].event_description
        }}</span>
      </div>
      <div class="relative -left-1 flex flex-col gap-y-3">
        <button
          v-for="(button, index) in EventsData[nowSwiperIndex].event_buttons"
          :key="index"
          :class="`w-full py-2 rounded-3xl ${button.buttonClass}`"
          @click="button.buttonCallback"
        >
          {{ button.buttonLabel }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Swiper as SwiperComponent, SwiperSlide } from "swiper/vue";
import { Swiper } from "swiper/types";
import { ref } from "vue";

import "swiper/css";

interface EventButton {
  buttonLabel: string;
  buttonClass: string;
  buttonCallback: () => void;
}

interface Event {
  event_photo: string;
  event_title: string;
  event_description: string;
  event_buttons: EventButton[];
}

const nowSwiperIndex = ref(0);

const EventsData = [
  {
    event_photo: "/img/card1.png",
    event_description:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatem, dolore alias! Cum saepe molestias reprehenderit",
    event_title: "PIPL SUNDAYS1",
    event_buttons: [
      {
        buttonLabel: "Получить проходку",
        buttonClass: "text-[#8d60d7]",
        buttonCallback: () => alert("quququ"),
      },
      {
        buttonLabel: "Забронировать стол",
        buttonClass: "bg-[#8d60d7]",
        buttonCallback: () => alert("Забронировать стол"),
      },
    ],
  },
  {
    event_photo: "/img/card1.png",
    event_description: "AAAAAAAAAAAAAAAAAAAAAAAAaaa",
    event_title: "PIPL SUNDAYS2",
  },
  {
    event_photo: "/img/card1.png",
    event_description: "sdklfnkdf snvklnfklvnk ldnfklvnkld fnklnvknnkln",
    event_title: "PIPL SUNDAYS3",
  },
] as Event[];

const onSwiper = (swiper: Swiper) => {
  nowSwiperIndex.value = swiper.activeIndex;
};
const onSlideChange = (swiper: Swiper) => {
  nowSwiperIndex.value = swiper.activeIndex;
  console.log(nowSwiperIndex);
};
</script>
 