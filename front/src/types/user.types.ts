export interface SelectedDate {
  selectedDay: string;
  selectedMonth: string;
  selectedYear: string;
}

export interface addUserType {
  tg_id: number;
  tg_name: string;
  tg_lastname: string;
  tg_username: string;
  date_birth: SelectedDate;
}

export interface BirthData {
  days_for_birth: number;
  minutes_for_birth: number;
  hours_for_birth: number;
}

export interface userDataType {
  id: number;
  tg_id: number;
  tg_name: string;
  tg_lastname: string;
  tg_username: string;
  birth_data: BirthData;
}

export class UserDataType implements userDataType {
  id: number;
  tg_id: number;
  tg_name: string;
  tg_lastname: string;
  tg_username: string;
  birth_data: BirthData;

  constructor(
    id: number,
    tg_id: number,
    tg_name: string,
    tg_lastname: string,
    tg_username: string,
    birth_data: BirthData
  ) {
    this.id = id;
    this.tg_id = tg_id;
    this.tg_name = tg_name;
    this.tg_lastname = tg_lastname;
    this.tg_username = tg_username;
    this.birth_data = birth_data;
  }
}
