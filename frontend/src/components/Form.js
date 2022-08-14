import React from "react";
import {
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  TextField,
} from "@mui/material";

const Form = (props) => {
  console.log(props);
  const attributes = Array.from(props?.attributes);
  const inpLabel = props?.inpLabel || "Criteria";
  const inpValues = props?.inpValues || [">", "<", ">=", "<=", "=="];

  return (
    <form
      action=""
      className="flex flex-row"
      style={{ display: "flex", justifyContent: "center" }}
    >
      <div className="attributes">
        <FormControl size="small" sx={{ m: 1, minWidth: 220 }}>
          <InputLabel id="demo-simple-select-label">Attributes</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            // value={10}
            label="Attributes"
            // onChange={handleChange}
          >
            {attributes &&
              attributes.map((attribute) => {
                return <MenuItem value={attribute}>{attribute}</MenuItem>;
              })}
          </Select>
        </FormControl>
      </div>

      <div className="criteria">
        <FormControl size="small" sx={{ m: 1, minWidth: 220 }}>
          <InputLabel id="demo-simple-select-label">{inpLabel}</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            // value={20}
            label="Criteria"
            // onChange={handleChange}
          >
            {inpValues &&
              inpValues.map((val) => {
                return <MenuItem value={val}>{val}</MenuItem>;
              })}
          </Select>
        </FormControl>
      </div>

      <div className="value">
        <TextField
          id="outlined-basic"
          label="Value"
          variant="outlined"
          size="small"
          sx={{ m: 1, minWidth: 220 }}
        />
      </div>
    </form>
  );
};

export default Form;
