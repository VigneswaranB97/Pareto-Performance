import {
  BrowserRouter as Router,
  Routes,
  Route,
  useRoutes,
} from "react-router-dom";
import Form from "./components/Form";
import Layout from "./components/Layout";

const App = () => {
  let routes = useRoutes([{ path: "/", element: <Form /> }]);
  return routes;
};

const AppWrapper = () => {
  return (
    <Router>
      <Layout />
      <App />
    </Router>
  );
};

export default AppWrapper;
