import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import CategoryPage from "./pages/CategoryPage";
import ProductPage from "./pages/ProductPage";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        {/* Home Page */}
        <Route
          path="/"
          element={<Home />}
        />

        {/* Service Category Page */}
        <Route
          path="/category/:category"
          element={<CategoryPage />}
        />

        {/* Product Details Page */}
        <Route
          path="/product/:id"
          element={<ProductPage />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;