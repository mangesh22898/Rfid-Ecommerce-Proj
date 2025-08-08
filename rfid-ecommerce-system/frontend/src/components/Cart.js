import React from "react";

export default function Cart({ cart }) {
  return (
    <div>
      <h2>Cart</h2>
      {cart.length === 0 ? (
        <p>No items in cart.</p>
      ) : (
        <ul>
          {cart.map((c, idx) => (
            <li key={idx}>
              {c.product?.name || c.product} - {c.qty || 1}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
