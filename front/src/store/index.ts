import { defineStore } from "pinia";
import { selectedDateType } from "../types/datePicker.types";
import { userDataType } from "../types/user.types";

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

export const useUserDataStore = defineStore("userData", {
  state: () => ({
    userData: null as userDataType | null,
  }),
  getters: {
    getUserData: (state) => {
      return state.userData;
    },
  },
  actions: {
    setUserData(userData: userDataType) {
      this.userData = userData;
    },
  },
});
