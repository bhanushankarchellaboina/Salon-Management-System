import axios from "axios";

const api = axios.create({
    baseURL: "https://salon-management-system-2rxa.onrender.com",
});

export default api;