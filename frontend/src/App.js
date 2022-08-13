import {
  BrowserRouter as Router,
  Routes,
  Route,
  useRoutes,
} from "react-router-dom";
import FormArray from "./components/FormArray";
import Layout from "./components/Layout";

const App = () => {
  let routes = useRoutes([{ path: "/", element: <FormArray /> }]);
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
