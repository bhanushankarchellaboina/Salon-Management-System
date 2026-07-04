import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../services/api";

function CategoryPage() {
    const { category } = useParams();

    const [services, setServices] = useState([]);

    useEffect(() => {
        fetchServices();
    }, []);

    const fetchServices = async () => {
        try {
            const response = await api.get(`/items/category/${category}`);
            setServices(response.data);
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <div className="container">

            <h1>{category}</h1>

            {services.map((service) => (
                <div
                    key={service.id}
                    style={{
                        background: "#1a1f2e",
                        marginBottom: "15px",
                        padding: "20px",
                        borderRadius: "10px",
                        color: "white"
                    }}
                >
                    <h3>{service.name}</h3>

                    <h2>₹ {service.price}</h2>

                </div>
            ))}

        </div>
    );
}

export default CategoryPage;