import React, { useState, useEffect } from "react";
import { getCatalog, getCart, addToCart, checkoutOrder } from "./api";
import Catalog from "./components/Catalog";
import Cart from "./components/Cart";
import Checkout from "./components/Checkout";

function App() {
  const [catalog, setCatalog] = useState([]);
  const [cart, setCart] = useState([]);
  const [form, setForm] = useState({
    name: "",
    institute: "",
    phone: "",
    email: "",
    room: ""
  });

  // Fetch initial data
  useEffect(() => {
    getCatalog().then(res => setCatalog(res.data));
    getCart().then(res => setCart(res.data));
  }, []);

  const handleFormChange = (key, value) => {
    setForm({ ...form, [key]: value });
  };

  const handleAddToCart = (product) => {
    const item = { ...form, product };
    addToCart(item).then(() => getCart().then(res => setCart(res.data)));
  };

  const handleCheckout = () => {
    checkoutOrder({ customer: form, items: cart }).then(() =>
      alert("Order placed!")
    );
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>RFID Business Cards</h1>
      <Catalog
        products={catalog}
        form={form}
        onFormChange={handleFormChange}
        onAdd={handleAddToCart}
      />
      <Cart cart={cart} />
      <Checkout onCheckout={handleCheckout} />
    </div>
  );
}

export default App;
