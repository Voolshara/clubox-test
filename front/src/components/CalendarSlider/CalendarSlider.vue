<template>
  <div class="relative flex flex-row w-5/6 h-80 text-lg">
    <div class="absolute w-full h-full flex items-center justify-center">
      <div class="border-y w-full h-14"></div>
    </div>
    <div
      ref="daySlider"
      class="custom-slider relative z-10 w-28 h-full overflow-y-scroll scroll-smooth flex flex-col gap-y-7 py-36"
      @scroll="onScroll('day')"
    >
      <CalendarSelectedItem
        v-for="(day, i) in days"
        :key="i"
        :label="day"
        :is-selected="selectedDate.selectedDay === day"
      />
    </div>
    <div
      ref="monthSlider"
      class="custom-slider relative z-10 w-full h-full overflow-y-scroll scroll-smooth flex flex-col gap-y-7 py-36"
      @scroll="onScroll('month')"
    >
      <CalendarSelectedItem
        v-for="(month, i) in months"
        :key="i"
        :label="month"
        :is-selected="selectedDate.selectedMonth === month"
      />
    </div>
    <div
      ref="yearSlider"
      class="custom-slider relative z-10 w-32 h-full overflow-y-scroll scroll-smooth flex flex-col gap-y-7 py-36"
      @scroll="onScroll('year')"
    >
      <CalendarSelectedItem
        v-for="(year, i) in years"
        :key="i"
        :label="year"
        :is-selected="selectedDate.selectedYear === year"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { reactive, ref } from "vue";
import { days, years, months } from "./dateData";
import CalendarSelectedItem from "./CalendarSelectedItem.vue";

interface selectedDateType {
  selectedDay: string;
  selectedMonth: string;
  selectedYear: string;
}

export default {
  components: { CalendarSelectedItem },
  setup() {
    let scrollTimeout: ReturnType<typeof setTimeout> | null = null;
    const now_date = new Date(Date.now());
    const selectedDate: selectedDateType = reactive({
      selectedDay: String(now_date.getDate()), // Use getDate() instead of getDay() for the actual day of the month
      selectedMonth: months[now_date.getMonth()],
      selectedYear: String(now_date.getFullYear()),
    });

    const daySlider = ref<HTMLDivElement | null>(null);
    const monthSlider = ref<HTMLDivElement | null>(null);
    const yearSlider = ref<HTMLDivElement | null>(null);

    const onScroll = (type: "day" | "month" | "year") => {
      if (scrollTimeout) {
        clearTimeout(scrollTimeout);
      }

      scrollTimeout = setTimeout(() => {
        centerSelected(type);
      }, 100);

      let slider: HTMLDivElement | null = null;
      if (type === "day") {
        slider = daySlider.value;
      } else if (type === "month") {
        slider = monthSlider.value;
      } else if (type === "year") {
        slider = yearSlider.value;
      }

      if (slider) {
        const sliderRect = slider.getBoundingClientRect();
        const centerY = sliderRect.top + sliderRect.height / 2;

        let closestElem: HTMLElement = slider.firstChild as HTMLElement;
        let minDistance = Infinity;

        slider.childNodes.forEach((child) => {
          if (child.nodeType === Node.ELEMENT_NODE) {
            const childElem = child as HTMLElement;
            const childRect = childElem.getBoundingClientRect();
            const childCenterY = childRect.top + childRect.height / 2;
            const distance = Math.abs(centerY - childCenterY);
            if (distance < minDistance) {
              minDistance = distance;
              closestElem = childElem;
            }
          }
        });

        const closestValue = closestElem?.textContent || "";
        if (type === "day") {
          selectedDate.selectedDay = closestValue;
        } else if (type === "month") {
          selectedDate.selectedMonth = closestValue;
        } else if (type === "year") {
          selectedDate.selectedYear = closestValue;
        }
      }
    };

    const centerSelected = (type: "day" | "month" | "year") => {
      let slider: HTMLDivElement | null = null;
      if (type === "day") {
        slider = daySlider.value;
      } else if (type === "month") {
        slider = monthSlider.value;
      } else if (type === "year") {
        slider = yearSlider.value;
      }

      if (slider) {
        const sliderRect = slider.getBoundingClientRect();
        const centerY = sliderRect.height / 2;

        let selectedValue = "";
        if (type === "day") selectedValue = selectedDate.selectedDay;
        if (type === "month") selectedValue = selectedDate.selectedMonth;
        if (type === "year") selectedValue = selectedDate.selectedYear;

        const selectedElem = Array.from(slider.childNodes).find((child) => {
          if (child.nodeType === Node.ELEMENT_NODE) {
            const childElem = child as HTMLElement;
            return childElem.textContent === selectedValue;
          }
          return false;
        }) as HTMLElement | undefined;

        if (selectedElem) {
          const selectedRect = selectedElem.getBoundingClientRect();
          const selectedCenterY =
            selectedRect.top - sliderRect.top + selectedRect.height / 2;
          const scrollTop = slider.scrollTop + selectedCenterY - centerY;

          slider.scrollTo({
            top: scrollTop,
            behavior: "smooth",
          });
        }
      }
    };

    return {
      selectedDate,
      days,
      months,
      years,
      daySlider,
      monthSlider,
      yearSlider,
      onScroll,
    };
  },
};
</script>

<style>
.custom-slider::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
.custom-slider {
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}
</style>
