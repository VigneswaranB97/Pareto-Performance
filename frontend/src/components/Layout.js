import React from "react";
import styled from "styled-components";
import { v, b } from "../styles/variables";
import Navbar from "./Navbar";

export const SMain = styled.main`
  transition: 0.3s ease padding;
  padding: ${v.mdSpacing} ${v.mdSpacing};

  @media ${b.sm} {
    padding: ${v.lgSpacing} ${v.mdSpacing};
  }

  @media ${b.lg} {
    padding: ${v.lgSpacing} ${v.lgSpacing};
    margin: 0 auto;
    width: 100%;
    max-width: ${v.lg};
  }

  /* display: flex;
    justify-content: center; */
`;

const Layout = ({ children }) => {
  return (
    <>
      <Navbar />
      <SMain>{children}</SMain>
    </>
  );
};

export default Layout;
