import { useNavigate } from "react-router-dom";

function ServiceCard({ service }) {

    const navigate = useNavigate();

    return (
        <div
            className="service-card"
            onClick={() => navigate(`/category/${service.category}`)}
        >
            <img
                src={service.image}
                alt={service.category}
                className="service-image"
            />

            <div className="service-content">
                <h3>{service.category}</h3>

                <p>Starting from</p>

                <h2>₹ {service.starting_price}</h2>
            </div>
        </div>
    );
}

export default ServiceCard;