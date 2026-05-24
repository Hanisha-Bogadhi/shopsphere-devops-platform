javascript
const products = [
  {
    id: 1,
    name: "iPhone 15",
    price: "₹79,999",
    image: "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9"
  },
  {
    id: 2,
    name: "Gaming Laptop",
    price: "₹1,09,999",
    image: "https://images.unsplash.com/photo-1496181133206-80ce9b88a853"
  },
  {
    id: 3,
    name: "Wireless Headphones",
    price: "₹5,999",
    image: "https://images.unsplash.com/photo-1505740420928-5e560c06d30e"
  },
  {
    id: 4,
    name: "Smart Watch",
    price: "₹12,999",
    image: "https://images.unsplash.com/photo-1523275335684-37898b6baf30"
  }
];

const productList = document.getElementById('product-list');
const cartCount = document.getElementById('cart-count');

let count = 0;

products.forEach(product => {
  const card = document.createElement('div');
  card.className = 'product-card';

  card.innerHTML = `
    <img src="${product.image}" alt="${product.name}">
    <h3>${product.name}</h3>
    <p class="price">${product.price}</p>
    <button onclick="addToCart()">Add to Cart</button>
  `;

  productList.appendChild(card);
});

function addToCart() {
  count++;
  cartCount.innerText = count;
}