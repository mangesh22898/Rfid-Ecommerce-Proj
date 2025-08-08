import React from "react";

export default function Catalog({ products, form, onFormChange, onAdd }) {
  return (
    <div>
      <h2>Customer Details</h2>
      {Object.keys(form).map((key) => (
        <input
          key={key}
          placeholder={key}
          value={form[key]}
          onChange={(e) => onFormChange(key, e.target.value)}
          style={{ margin: "5px", padding: "5px" }}
        />
      ))}

      <h2>Catalog</h2>
      <ul>
        {products.map((p, idx) => (
          <li key={idx}>
            {p.name} - {p.price}
            <button onClick={() => onAdd(p)}>Add</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
