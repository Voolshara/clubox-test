export interface addUserType {
  tg_id: number;
  tg_name: string;
  tg_lastname: string;
  tg_username: string;
  date_birth: Date;
}

export interface userDataType {
  id: number;
  tg_id: number;
  tg_name: string;
  tg_lastname: string;
  tg_username: string;
  days_for_birth: number;
}

export class UserDataType implements userDataType {
  id: number;
  tg_id: number;
  tg_name: string;
  tg_lastname: string;
  tg_username: string;
  days_for_birth: number;

  constructor(
    id: number,
    tg_id: number,
    tg_name: string,
    tg_lastname: string,
    tg_username: string,
    days_for_birth: number
  ) {
    this.id = id;
    this.tg_id = tg_id;
    this.tg_name = tg_name;
    this.tg_lastname = tg_lastname;
    this.tg_username = tg_username;
    this.days_for_birth = days_for_birth;
  }
}
