import { defineStore } from "pinia";
import { selectedDateType } from "../types/datePicker.types";

export const useSelectedDateStore = defineStore("selectDate", {
  state: () => ({
    selectDate: {
      selectedDay: "",
      selectedMonth: "",
      selectedYear: "",
    } as selectedDateType,
  }),
  getters: {
    getSelectedDate: (state) => state.selectDate,
  },
  actions: {
    setSelectedDate(selectDate: selectedDateType) {
      this.selectDate = selectDate;
    },
  },
});
