from flask import Flask

app = Flask(__name__)

@app.route('/products')
def products():

    return """

    <!DOCTYPE html>

    <html>

    <head>

        <title>Products</title>

        <style>

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {

                font-family: Arial, sans-serif;

                background: #f5f5f5;

                padding: 40px;
            }

            h1 {

                text-align: center;

                margin-bottom: 50px;

                font-size: 52px;
            }

            .products-grid {

                display: grid;

                grid-template-columns: repeat(3, 1fr);

                gap: 30px;
            }

            .product-card {

                background: white;

                border-radius: 12px;

                overflow: hidden;

                box-shadow: 0 4px 12px rgba(0,0,0,0.1);

                transition: 0.3s;
            }

            .product-card:hover {

                transform: translateY(-8px);
            }

            .product-card img {

                width: 100%;

                height: 260px;

                object-fit: cover;
            }

            .content {

                padding: 20px;
            }

            h2 {

                margin-bottom: 10px;
            }

            .price {

                color: #ef4444;

                font-size: 24px;

                font-weight: bold;

                margin-bottom: 15px;
            }

            button {

                width: 100%;

                padding: 14px;

                border: none;

                background: #111827;

                color: white;

                font-size: 16px;

                cursor: pointer;

                border-radius: 8px;
            }

            button:hover {

                background: #ef4444;
            }

        </style>

    </head>

    <body>

        <h1>All Products</h1>

        <div class="products-grid">

            <div class="product-card">

                <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=1000&q=80">

                <div class="content">

                    <h2>Nike Running Shoes</h2>

                    <p class="price">$120</p>

                    <button onclick="window.location.href='/cart'">
                        Add to Cart
                    </button>

                </div>

            </div>

            <div class="product-card">

                <img src="https://images.unsplash.com/photo-1523381210434-271e8be1f52b?auto=format&fit=crop&w=1000&q=80">

                <div class="content">

                    <h2>Casual Hoodie</h2>

                    <p class="price">$80</p>

                    <button onclick="window.location.href='/cart'">
                        Add to Cart
                    </button>

                </div>

            </div>

            <div class="product-card">

                <img src="https://images.unsplash.com/photo-1529139574466-a303027c1d8b?auto=format&fit=crop&w=1000&q=80">

                <div class="content">

                    <h2>Women's Jacket</h2>

                    <p class="price">$150</p>

                    <button onclick="window.location.href='/cart'">
                        Add to Cart
                    </button>

                </div>

            </div>

            <div class="product-card">

                <img src="https://images.unsplash.com/photo-1548036328-c9fa89d128fa?auto=format&fit=crop&w=1000&q=80">

                <div class="content">

                    <h2>Leather Bag</h2>

                    <p class="price">$200</p>

                    <button onclick="window.location.href='/cart'">
                        Add to Cart
                    </button>

                </div>

            </div>

            <div class="product-card">

                <img src="https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&fit=crop&w=1000&q=80">

                <div class="content">

                    <h2>Women's Fashion</h2>

                    <p class="price">$95</p>

                    <button onclick="window.location.href='/cart'">
                        Add to Cart
                    </button>


                </div>

            </div>

            <div class="product-card">

                <img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=1000&q=80">

                <div class="content">

                    <h2>Wireless Headphones</h2>

                    <p class="price">$180</p>

                    <button onclick="window.location.href='/cart'">
                        Add to Cart
                    </button>

                </div>
            
            </div>

        </div>

    </body>

    </html>

    """

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5001)