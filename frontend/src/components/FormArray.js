import React, { useState, Fragment } from "react";
import styled from "styled-components";
import Card from "@mui/material/Card";
import Form from "./Form";

// import CardActions from '@mui/material/CardActions';
import CardContent from "@mui/material/CardContent";
// import Button from '@mui/material/Button';
import Typography from "@mui/material/Typography";
import AddBoxIcon from "@mui/icons-material/AddBox";

const Container = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
`;

// const Card = styled.div`
//   border: 1px solid black;
//   border-radius: 6px;
//   width: 50%;
//   height: auto;
// `;

const FormArray = () => {
  let [numOfForms, setNumOfForms] = useState(1);

  const addForm = () => {
    let forms = numOfForms + 1;
    setNumOfForms(forms);
  };

  return (
    <Container>
      <Card sx={{ width: "80%" }}>
        <CardContent>
          <Typography variant="h5" component="div">
            Filters
          </Typography>
          <div
            style={{
              display: "flex",
              flexWrap: "wrap",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            {(() => {
              const options = [];

              for (let i = 0; i < numOfForms; i++) {
                options.push(
                  <Fragment key={i + 1}>
                    <Form /> <br />
                  </Fragment>
                );
              }

              return options;
            })()}
          </div>
          <button
            onClick={addForm}
            style={{
              fontSize: "1rem",
              margin: "1rem auto",
              display: "block",
              padding: "0.3rem",
              background: "black",
              color: "white",
              border: "1px solid black",
              borderRadius: "5px",
            }}
          >
            Add new Form
          </button>
          <hr />
          <Typography variant="h5" component="div">
            Attributes
          </Typography>
          <Typography sx={{ mb: 1.5 }} color="text.secondary">
            Form
          </Typography>
        </CardContent>
      </Card>
    </Container>
  );
};

export default FormArray;
