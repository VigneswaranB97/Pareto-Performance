import React, { useState, Fragment } from "react";
import styled from "styled-components";
import Card from "@mui/material/Card";
import Form from "./Form";
import ImportJson from "./Import";

import CardContent from "@mui/material/CardContent";

import Typography from "@mui/material/Typography";

const Container = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
`;

const buttonStyle = {
  fontSize: "1rem",
  margin: "1rem auto",
  display: "block",
  padding: "0.3rem 0.6rem",
  background: "black",
  color: "white",
  border: "1px solid black",
  borderRadius: "3px",
  cursor: "pointer",
};

const FormArray = () => {
  let [numOfForms, setNumOfForms] = useState(1);
  const [companyData, setCompanyData] = useState(null);
  const [alert, setAlert] = useState(null);

  const addForm = () => {
    let forms = numOfForms + 1;
    setNumOfForms(forms);
  };

  const attributesSet = new Set();

  const processJson = (val) => {
    console.log(val);
    try {
      JSON.parse(val);
      setAlert({ msg: "JSON imported successfully!!", type: "success" });
      setCompanyData(val);
    } catch (e) {
      console.log("invalid", e);
      setAlert({ msg: "Please import valid JSON", type: "danger" });
    }

    console.log("company data", companyData);
    console.log(val);
    const suppliers = val["suppliers"];
    console.log("suppliers", suppliers);
    suppliers.foreach((supplier) => {
      Object.keys(supplier).forEach((supplierKey) => {
        if (!attributesSet.has(supplierKey)) {
          attributesSet.add(supplierKey);
        }
      });
    });
  };

  return (
    <>
      {alert && (
        <p
          className={
            alert.type === "success"
              ? "p-2 block mx-auto mt-0 mb-3 w-3/4 bg-green-600/90 border rounded text-white"
              : "p-2 block mx-auto mt-0 mb-3 w-3/4 bg-red-500/80 border rounded text-white"
          }
        >
          {alert.msg}
        </p>
      )}
      <Container>
        <Card sx={{ width: "80%" }}>
          <CardContent>
            <Typography variant="h5" component="div">
              Upload Data
            </Typography>
            <div
              style={{
                display: "flex",
                flexWrap: "wrap",
                justifyContent: "center",
                alignItems: "center",
              }}
            >
              <ImportJson processJson={processJson} />
            </div>
            <hr />
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
                      <Form attributes={attributesSet} /> <br />
                    </Fragment>
                  );
                }

                return options;
              })()}
            </div>
            <button onClick={addForm} style={buttonStyle}>
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
    </>
  );
};

export default FormArray;
