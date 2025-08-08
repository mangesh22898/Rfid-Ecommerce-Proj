import axios from "axios";

// For now, these point to localhost; later Ingress URLs
const BASE_URLS = {
  catalog: "http://localhost:8000/api/catalog",
  cart: "http://localhost:8001/api/cart",
  checkout: "http://localhost:8002/api/checkout"
};

export const getCatalog = () => axios.get(BASE_URLS.catalog);
export const getCart = () => axios.get(BASE_URLS.cart);
export const addToCart = (item) => axios.post(BASE_URLS.cart, item);
export const checkoutOrder = (order) => axios.post(BASE_URLS.checkout, order);
