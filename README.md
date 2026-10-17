# KrishiMart-YourTrusted-Partner-in-Smart-Farming
# KrishiMart — Your Trusted Partner in Smart Farming
Frontend-only Streamlit demo of an agriculture marketplace. No database, backend, or APIs.

## Setup
1. Install Python 3.9+ from https://www.python.org/downloads/ (tick "Add Python to PATH").
2. Open this folder in VS Code (File > Open Folder), then open a terminal (Ctrl+`).
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `streamlit run app.py`

## Demo credentials
- Buyer: `buyer` / `buyer123`
- Seller: `seller` / `seller123`

## Test each feature
- **Home**: hero, featured products, quick-link buttons, disclaimer.
- **Marketplace**: search "urea", filter by category, try a nonsense search (empty message), add to cart.
- **Shopping Cart**: use ➕ ➖ 🗑️, try exceeding stock, Clear Cart, Demo Checkout.
- **Login**: wrong password shows an error; log in as Buyer or Seller; Logout.
- **Seller Dashboard**: log in as seller, add a product (try invalid price), then find it in the Marketplace.
- **Crop Doctor**: pick a crop, upload an image, click "Check Sample Result" (simulated only).
- **MP Crop Guide / Fertilizer Knowledge Center**: browse crop tabs and the fertilizer selector.

Note: data resets when the browser session restarts.
