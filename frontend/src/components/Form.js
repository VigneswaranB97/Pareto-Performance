import React from "react";
import {
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  TextField,
} from "@mui/material";

const Form = () => {
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
            <MenuItem value={10}>Ten</MenuItem>
            <MenuItem value={20}>Twenty</MenuItem>
            <MenuItem value={30}>Thirty</MenuItem>
          </Select>
        </FormControl>
      </div>

      <div className="criteria">
        <FormControl size="small" sx={{ m: 1, minWidth: 220 }}>
          <InputLabel id="demo-simple-select-label">Criteria</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            // value={20}
            label="Criteria"
            // onChange={handleChange}
          >
            <MenuItem value={10}>Greater than</MenuItem>
            <MenuItem value={20}>Lesser than</MenuItem>
            <MenuItem value={30}>Greater than or equal to</MenuItem>
            <MenuItem value={30}>Lesser than or equal to</MenuItem>
            <MenuItem value={30}>Equals to</MenuItem>
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
