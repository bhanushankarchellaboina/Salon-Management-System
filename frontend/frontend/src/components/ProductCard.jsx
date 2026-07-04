import { useNavigate } from "react-router-dom";

function ProductCard({ product }) {

    const navigate = useNavigate();

    return (

        <div
            className="service-card"
            onClick={() => navigate(`/product/${product.id}`)}
        >

            <img
                src={product.image}
                alt={product.name}
                className="service-image"
            />

            <div className="service-content">

                <h3>{product.name}</h3>

                <p>{product.purpose}</p>

                <h2>₹ {product.price}</h2>

            </div>

        </div>

    );
}

export default ProductCard;