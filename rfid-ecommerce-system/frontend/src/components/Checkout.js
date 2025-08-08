import React from "react";

export default function Checkout({ onCheckout }) {
  return (
    <div>
      <button onClick={onCheckout} style={{ marginTop: "10px" }}>
        Checkout
      </button>
    </div>
  );
}
