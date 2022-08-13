import React, { useState } from "react";

const ImportJson = (props) => {
  const processJson = (e) => {
    props.processJson(e.target.value);
  };

  return (
    <form style={{ width: "100%" }}>
      <div
        className="importJson"
        style={{
          marginBottom: "1rem",
        }}
      >
        <textarea
          name="json"
          id=""
          rows="15"
          onChange={processJson}
          style={{
            width: "70%",
            margin: "auto",
            display: "block",
            border: "0.5px solid rgba(0, 0, 0, 0.6)",
            borderRadius: "3px",
            padding: "1rem",
          }}
        ></textarea>
      </div>
    </form>
  );
};

export default ImportJson;
