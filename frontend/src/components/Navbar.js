import FunctionsOutlinedIcon from "@mui/icons-material/FunctionsOutlined";
import React from "react";
import styled from "styled-components";

const Container = styled.div`
  height: 60px;
`;

const Wrapper = styled.div`
  padding: 10px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
`;

const Left = styled.div`
  flex: 1;
  display: flex;
  align-items: center;
`;

const Right = styled.div`
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: flex-end;
`;

const Center = styled.div`
  flex: 1;
  text-align: center;
`;

const Logo = styled.h1`
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: center;
`;

const Navbar = () => {
  return (
    <Container>
      <Wrapper>
        <Left></Left>
        <Center>
          <Logo>
            <FunctionsOutlinedIcon sx={{ fontSize: 70 }} />
            PareTo.
          </Logo>
        </Center>
        <Right>
          {/* <MenuItem>
            <Link href="/register">REGISTER</Link>
          </MenuItem>
          <MenuItem>
            <Link href="/signin">SIGN IN</Link>
          </MenuItem>
          <MenuItem>
            <PersonOutlineIcon />
          </MenuItem> */}
        </Right>
      </Wrapper>
    </Container>
  );
};

export default Navbar;
