from flask import Flask

app = Flask(__name__)

@app.route('/cart')
def cart():

    return """

    <!DOCTYPE html>

    <html>

    <head>

        <title>Shopping Cart</title>

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

                font-size: 50px;

                color: #111827;
            }

            .cart-container {

                max-width: 1100px;

                margin: auto;

                background: white;

                border-radius: 12px;

                padding: 30px;

                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }

            .cart-item {

                display: flex;

                align-items: center;

                justify-content: space-between;

                margin-bottom: 30px;

                padding-bottom: 20px;

                border-bottom: 1px solid #ddd;
            }

            .cart-left {

                display: flex;

                align-items: center;

                gap: 20px;
            }

            .cart-left img {

                width: 140px;

                height: 140px;

                object-fit: cover;

                border-radius: 10px;
            }

            .cart-details h2 {

                margin-bottom: 10px;
            }

            .price {

                color: #ef4444;

                font-size: 24px;

                font-weight: bold;
            }

            .quantity {

                font-size: 18px;

                margin-top: 10px;
            }

            .summary {

                margin-top: 40px;

                text-align: right;
            }

            .summary h2 {

                font-size: 36px;

                margin-bottom: 20px;
            }

            button {

                padding: 15px 40px;

                border: none;

                background: #111827;

                color: white;

                font-size: 18px;

                cursor: pointer;

                border-radius: 8px;
            }

            button:hover {

                background: #ef4444;
            }

        </style>

    </head>

    <body>

        <h1>Your Shopping Cart</h1>

        <div class="cart-container">

            <div class="cart-item">

                <div class="cart-left">

                    <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=1000&q=80">

                    <div class="cart-details">

                        <h2>Nike Running Shoes</h2>

                        <p class="price">$120</p>

                        <p class="quantity">Quantity: 1</p>

                    </div>

                </div>

            </div>

            <div class="cart-item">

                <div class="cart-left">

                    <img src="https://images.unsplash.com/photo-1548036328-c9fa89d128fa?auto=format&fit=crop&w=1000&q=80">

                    <div class="cart-details">

                        <h2>Leather Bag</h2>

                        <p class="price">$200</p>

                        <p class="quantity">Quantity: 1</p>

                    </div>

                </div>

            </div>

            <div class="summary">

                <h2>Total: $320</h2>

                <button>
                    Proceed To Checkout
                </button>

            </div>

        </div>

    </body>

    </html>

    """

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)