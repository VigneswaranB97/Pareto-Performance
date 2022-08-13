import React from "react";
import styled from "styled-components";
import Card from "@mui/material/Card";
// import CardActions from '@mui/material/CardActions';
import CardContent from "@mui/material/CardContent";
// import Button from '@mui/material/Button';
import Typography from "@mui/material/Typography";

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

const Form = () => {
  return (
    <Container>
      <Card sx={{ minWidth: 378 }}>
        <CardContent>
          <Typography variant="h5" component="div">
            Filters
          </Typography>
          <Typography sx={{ mb: 1.5 }} color="text.secondary">
            Form
          </Typography>
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

export default Form;
