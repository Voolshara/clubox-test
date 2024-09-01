import { useUserDataStore } from "../store";
import { userDataType } from "../types/user.types";

export const getUserData = async (tg_id: String) => {
  const store = useUserDataStore();

  const response = await fetch(`http://127.0.0.1:8000/user/${tg_id}`);
  if (response.status === 200) {
    const data = (await response.json()) as userDataType;
    store.setUserData(data);
  }
  return {};
};
