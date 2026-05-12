import axios from "axios";

// const API_URL = "http://127.0.0.1:8000/api/user";
const API_URL = "http://localhost:8000/api/user";

export const getUsers = async (
  q = "",
  start = 0,
  limit = 10
) => {

  const response = await axios.get(API_URL, {
    params: {
      q,
      start,
      limit,
    },
  });

  return response.data;
};


export const createUser = async (userData) => {

  const response = await axios.post(
    API_URL,
    userData
  );

  return response.data;
};


export const updateUser = async (
  userId,
  userData
) => {

  const response = await axios.put(
    `${API_URL}/${userId}`,
    userData
  );

  return response.data;
};


export const deleteUser = async (userId) => {

  const response = await axios.delete(
    `${API_URL}/${userId}`
  );

  return response.data;
};