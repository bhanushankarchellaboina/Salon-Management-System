import { useEffect, useState } from "react";
import { FaMoon, FaSun } from "react-icons/fa";

import api from "../services/api";
import ServiceCard from "../components/ServiceCard";
import ProductCard from "../components/ProductCard";
import About from "../components/About";

function Home() {

    const [services, setServices] = useState([]);
    const [products, setProducts] = useState([]);

    // Theme State
    const [theme, setTheme] = useState(
        localStorage.getItem("theme") || "dark"
    );

    // Apply theme whenever it changes
    useEffect(() => {

        document.body.className = "";

        if (theme === "light") {
            document.body.classList.add("light-theme");
        }

        localStorage.setItem("theme", theme);

    }, [theme]);

    // Fetch data once
    useEffect(() => {
        fetchServices();
        fetchProducts();
    }, []);

    // Toggle Theme
    const toggleTheme = () => {
        setTheme(theme === "dark" ? "light" : "dark");
    };

    // Fetch Services
    const fetchServices = async () => {
        try {
            const response = await api.get("/items/categories");
            setServices(response.data);
        } catch (error) {
            console.log(error);
        }
    };

    // Fetch Products
    const fetchProducts = async () => {
        try {
            const response = await api.get("/products");
            setProducts(response.data);
        } catch (error) {
            console.log(error);
        }
    };

    return (

        <div className="container">

            {/* Navbar */}

            <div className="navbar">

                <button
                    className="theme-btn"
                    onClick={toggleTheme}
                >

                    {theme === "dark" ? <FaSun /> : <FaMoon />}

                </button>

                <a href="#about" className="about-link">
                    About
                </a>

            </div>

            {/* Hero */}

            <h1>Suma Beauty Salon Services</h1>

            <p className="subtitle">
                Makes Your Beauty Shine
            </p>

            {/* Services */}

            <div className="card-container">

                {services.map((service) => (

                    <ServiceCard
                        key={service.category}
                        service={service}
                    />

                ))}

            </div>

            {/* Products */}

            <h1 style={{ marginTop: "90px" }}>
                Beauty Products
            </h1>

            <p className="subtitle">
                Premium salon products for glowing skin and healthy hair
            </p>

            <div className="card-container">

                {products.map((product) => (

                    <ProductCard
                        key={product.id}
                        product={product}
                    />

                ))}

            </div>

            {/* About */}

            <About />

        </div>

    );
}

export default Home;