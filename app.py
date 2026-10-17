import random
import streamlit as st

st.set_page_config(page_title="KrishiMart — Your Trusted Partner in Smart Farming", page_icon="🌾", layout="wide")

PAGES = ["Home", "Marketplace", "Shopping Cart", "Crop Doctor", "MP Crop Guide",
         "Fertilizer Knowledge Center", "Login", "Seller Dashboard"]
CATEGORIES = ["Seeds", "Fertilizers", "Farming Tools", "Crop Protection"]
USERS = {"Buyer": ("buyer", "buyer123"), "Seller": ("seller", "seller123")}

PRODUCTS = [
    {"name": "Certified Wheat Seeds (10 kg)", "category": "Seeds", "price": 650, "desc": "High-yield, rust-tolerant wheat variety.", "seller": "Demo Seller", "stock": 40, "emoji": "🌾"},
    {"name": "Soybean Seeds (30 kg)", "category": "Seeds", "price": 2400, "desc": "Quality soybean seed with good germination.", "seller": "Narmada Agro", "stock": 25, "emoji": "🫘"},
    {"name": "Gram (Chana) Seeds (20 kg)", "category": "Seeds", "price": 1900, "desc": "Bold-grain chickpea seed for rabi sowing.", "seller": "Demo Seller", "stock": 30, "emoji": "🌱"},
    {"name": "Mustard Seeds (5 kg)", "category": "Seeds", "price": 780, "desc": "Oil-rich mustard variety for rabi season.", "seller": "Malwa Seeds Co.", "stock": 50, "emoji": "🌼"},
    {"name": "Neem-Coated Urea (45 kg)", "category": "Fertilizers", "price": 270, "desc": "Nitrogen source with slow release.", "seller": "Narmada Agro", "stock": 100, "emoji": "🧪"},
    {"name": "Vermicompost (25 kg)", "category": "Fertilizers", "price": 450, "desc": "Organic compost that improves soil health.", "seller": "Demo Seller", "stock": 60, "emoji": "🪱"},
    {"name": "SSP Fertilizer (50 kg)", "category": "Fertilizers", "price": 520, "desc": "Phosphorus and sulphur for oilseeds and pulses.", "seller": "Malwa Seeds Co.", "stock": 45, "emoji": "🧂"},
    {"name": "Hand Sprayer (16 L)", "category": "Farming Tools", "price": 1150, "desc": "Knapsack sprayer for pesticides and nutrients.", "seller": "Kisan Tools", "stock": 20, "emoji": "🎒"},
    {"name": "Steel Sickle (Hasiya)", "category": "Farming Tools", "price": 180, "desc": "Durable serrated sickle for harvesting.", "seller": "Kisan Tools", "stock": 80, "emoji": "🔪"},
    {"name": "Garden Hoe (Kudali)", "category": "Farming Tools", "price": 320, "desc": "Strong hoe for weeding and soil work.", "seller": "Demo Seller", "stock": 35, "emoji": "⛏️"},
    {"name": "Neem Oil Bio-Pesticide (1 L)", "category": "Crop Protection", "price": 420, "desc": "Plant-based protection against sucking pests.", "seller": "Narmada Agro", "stock": 55, "emoji": "🛡️"},
    {"name": "Pheromone Trap Kit (5 pcs)", "category": "Crop Protection", "price": 360, "desc": "Monitors and traps pod borer moths.", "seller": "Malwa Seeds Co.", "stock": 28, "emoji": "🪤"},
]

CROPS = {
    "Wheat": {"issue": "Yellow Rust", "symptoms": "Yellow-orange powdery stripes on leaves; reduced grain filling.",
              "prevention": "Use resistant varieties, avoid late sowing, scout fields in cool humid weather.",
              "season": "Rabi (Oct–Mar)", "sowing": "Early to late November (irrigated)", "soil": "Well-drained loam to clay loam, pH 6.5–7.5",
              "irrigation": "Critical stages: crown root initiation, tillering, flowering and grain filling.",
              "care": "Timely weeding, balanced nutrition based on soil test, watch for rust in January."},
    "Soybean": {"issue": "Yellow Mosaic Virus (whitefly-spread)", "symptoms": "Yellow patches on leaves, stunted growth, fewer pods.",
                "prevention": "Remove infected plants, control whiteflies, use tolerant varieties, rotate crops.",
                "season": "Kharif (Jun–Oct)", "sowing": "Mid-June to early July after good monsoon rains", "soil": "Well-drained medium black soil, pH 6.0–7.5",
                "irrigation": "Mostly rainfed; protective irrigation during dry spells at flowering and pod filling.",
                "care": "Ensure drainage, intercultural operations at 20–30 days, monitor stem fly and girdle beetle."},
    "Gram": {"issue": "Wilt (Fusarium)", "symptoms": "Drooping and yellowing plants, drying of whole plants in patches.",
             "prevention": "Seed treatment, resistant varieties, long crop rotation, avoid waterlogging.",
             "season": "Rabi (Oct–Mar)", "sowing": "Mid-October to mid-November", "soil": "Well-drained loam to clay loam, avoid saline soils",
             "irrigation": "Needs few irrigations; one at branching and one at pod filling if rain is scarce.",
             "care": "Nipping tips at 30–40 days, pheromone traps for pod borer, avoid excess nitrogen."},
    "Mustard": {"issue": "Aphids / White Rust", "symptoms": "Clusters of small insects on stems and pods; white blisters on leaves.",
                "prevention": "Timely sowing, balanced fertilizer, field sanitation, early scouting for aphids.",
                "season": "Rabi (Oct–Mar)", "sowing": "Early to late October", "soil": "Sandy loam to loam, well-drained, pH 6.5–8.0",
                "irrigation": "One or two irrigations at branching and siliqua formation.",
                "care": "Thin plants to proper spacing, sulphur supply helps oil content, watch for aphids in cloudy weather."},
}

FERTS = {
    "Urea": {"purpose": "Quick nitrogen source for leafy growth.", "nutrients": "About 46% N.",
             "precautions": "Over-use burns crops and pollutes water; avoid applying before heavy rain.", "handling": "Store dry, wear gloves, keep away from children."},
    "DAP": {"purpose": "Phosphorus and nitrogen for root development at sowing.", "nutrients": "About 18% N, 46% P₂O₅.",
            "precautions": "Place near seed, not in direct contact; avoid excess phosphorus.", "handling": "Keep bags sealed and dry; wash hands after use."},
    "NPK": {"purpose": "Balanced nutrition when all three major nutrients are needed.", "nutrients": "Nitrogen, phosphorus and potassium in varying grades (e.g., 12:32:16).",
            "precautions": "Choose the grade as per soil test; don't mix with incompatible products.", "handling": "Store in a cool dry place; use a mask while spreading."},
    "SSP": {"purpose": "Phosphorus plus sulphur and calcium; good for oilseeds and pulses.", "nutrients": "About 16% P₂O₅, 11% S, 19% Ca.",
            "precautions": "Apply as basal dose; may cake if damp.", "handling": "Keep dry, avoid dust inhalation."},
    "Organic Compost": {"purpose": "Improves soil structure, water holding and microbial life.", "nutrients": "Low but wide range of nutrients (about 0.5–1.5% N).",
                        "precautions": "Use well-decomposed compost only; raw manure can harm seedlings.", "handling": "Turn the pile regularly; wash hands after handling."},
    "Vermicompost": {"purpose": "Nutrient-rich organic manure from earthworm digestion.", "nutrients": "About 1.5–2% N plus P, K and micronutrients.",
                     "precautions": "Keep moist, not waterlogged; protect from direct sun.", "handling": "Store in shade; light and safe to handle."},
    "Neem-Coated Urea": {"purpose": "Urea coated with neem oil to slow nitrogen release and reduce losses.", "nutrients": "About 46% N.",
                         "precautions": "Still a strong fertilizer; apply only as advised for crop and soil.", "handling": "Store dry, wear gloves, avoid skin contact."},
}

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@600;800&family=Nunito:wght@400;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
.stApp { background: #FBF7EC; }
h1, h2, h3 { font-family: 'Fraunces', serif !important; color: #14532D !important; }
[data-testid="stSidebar"] { background: #14532D; }
[data-testid="stSidebar"] * { color: #FBF7EC !important; }
.hero { background: linear-gradient(135deg, #14532D 0%, #2F7D32 70%, #4C9A2A 100%); color: #fff; padding: 3rem 2rem; border-radius: 24px; margin-bottom: 1.5rem; }
.hero h1 { color: #fff !important; font-size: 3rem; margin: 0; }
.hero p { font-size: 1.15rem; color: #E8F3DC; margin-top: .6rem; }
.card { background: #fff; border: 1px solid #E3DCC4; border-radius: 18px; padding: 1rem 1.1rem; margin-bottom: .5rem; min-height: 190px; }
.card .emoji { font-size: 2.4rem; }
.card .title { font-weight: 700; color: #14532D; font-size: 1.05rem; }
.card .price { color: #2F7D32; font-weight: 800; font-size: 1.2rem; }
.card .meta { color: #6B6B5A; font-size: .85rem; }
.tag { display: inline-block; background: #E8F3DC; color: #14532D; border-radius: 999px; padding: 2px 10px; font-size: .75rem; font-weight: 700; }
.stButton > button { background: #2F7D32; color: #fff; border: 0; border-radius: 12px; font-weight: 700; }
.stButton > button:hover { background: #14532D; color: #fff; }
.info { background: #fff; border-left: 6px solid #4C9A2A; border-radius: 12px; padding: .8rem 1.1rem; margin-bottom: .6rem; }
@media (max-width: 640px) { .hero h1 { font-size: 2rem; } }
</style>
"""


def init_state():
    defaults = {"page": "Home", "role": None, "cart": {}, "products": [dict(p) for p in PRODUCTS], "order": None}
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def go(page):
    st.session_state.page = page


def find(name):
    return next((p for p in st.session_state.products if p["name"] == name), None)


def cart_total():
    return sum(find(n)["price"] * q for n, q in st.session_state.cart.items() if find(n))


# ---------- cart actions ----------
def add_to_cart(name):
    p = find(name)
    have = st.session_state.cart.get(name, 0)
    if p and have < p["stock"]:
        st.session_state.cart[name] = have + 1
        st.toast(f"Added {p['name']} to cart", icon="🛒")
    else:
        st.toast("Not enough stock available", icon="⚠️")


def change_qty(name, delta):
    p = find(name)
    new = st.session_state.cart.get(name, 0) + delta
    if new <= 0:
        st.session_state.cart.pop(name, None)
    elif p and new <= p["stock"]:
        st.session_state.cart[name] = new
    else:
        st.toast("Cannot exceed available stock", icon="⚠️")


def remove_item(name):
    st.session_state.cart.pop(name, None)


def clear_cart():
    st.session_state.cart = {}


def checkout():
    items = [(find(n), q) for n, q in st.session_state.cart.items() if find(n)]
    for p, q in items:
        p["stock"] -= q
    st.session_state.order = {"id": f"KM{random.randint(10000, 99999)}", "total": cart_total(), "count": sum(q for _, q in items)}
    st.session_state.cart = {}


# ---------- UI helpers ----------
def product_card(p, key):
    st.markdown(
        f"""<div class="card"><div class="emoji">{p['emoji']}</div>
        <div class="title">{p['name']}</div><span class="tag">{p['category']}</span>
        <div class="meta">{p['desc']}</div>
        <div class="price">₹{p['price']:,}</div>
        <div class="meta">Seller: {p['seller']} · Stock: {p['stock']}</div></div>""",
        unsafe_allow_html=True)
    if p["stock"] > 0:
        st.button("Add to Cart 🛒", key=key, on_click=add_to_cart, args=(p["name"],), use_container_width=True)
    else:
        st.button("Out of stock", key=key, disabled=True, use_container_width=True)


def product_grid(items, prefix):
    for i in range(0, len(items), 3):
        cols = st.columns(3)
        for col, p in zip(cols, items[i:i + 3]):
            with col:
                product_card(p, f"{prefix}_{p['name']}")


def info_box(title, text):
    st.markdown(f'<div class="info"><b>{title}</b><br>{text}</div>', unsafe_allow_html=True)


# ---------- pages ----------
def page_home():
    st.markdown("""<div class="hero"><h1>Grow Better. Farm Smarter.</h1>
        <p>KrishiMart brings seeds, fertilizers, tools and crop knowledge together for farmers across Madhya Pradesh.</p></div>""",
                unsafe_allow_html=True)
    st.subheader("Featured products")
    product_grid(st.session_state.products[:3], "home")
    st.subheader("Explore")
    links = ["Marketplace", "Shopping Cart", "Crop Doctor", "MP Crop Guide", "Fertilizer Knowledge Center", "Login"]
    cols = st.columns(3)
    for i, name in enumerate(links):
        cols[i % 3].button(name, key=f"ql_{name}", on_click=go, args=(name,), use_container_width=True)
    st.subheader("About")
    st.write("KrishiMart is a learning-friendly demo of an agriculture marketplace with crop and fertilizer guides.")
    st.info("Demo disclaimer: this is a frontend demonstration. There are no real payments, orders, logins, or AI diagnosis. "
            "Consult a qualified local agricultural expert before making farming decisions.")


def page_market():
    st.header("🛒 Marketplace")
    c1, c2 = st.columns([2, 1])
    q = c1.text_input("Search products", placeholder="e.g. wheat, urea, sprayer").strip().lower()
    cat = c2.selectbox("Category", ["All"] + CATEGORIES)
    items = [p for p in st.session_state.products
             if (cat == "All" or p["category"] == cat) and (q in p["name"].lower() or q in p["desc"].lower() or q in p["category"].lower())]
    if not items:
        st.warning("No products match your search. Try a different word or category.")
        return
    st.caption(f"{len(items)} product(s) found")
    product_grid(items, "mk")


def page_cart():
    st.header("🧺 Shopping Cart")
    order = st.session_state.order
    if order:
        st.success(f"✅ Demo order {order['id']} confirmed! {order['count']} item(s), total ₹{order['total']:,}. "
                   "This is a simulation — no payment was taken.")
        st.balloons()
        st.session_state.order = None
    cart = {n: q for n, q in st.session_state.cart.items() if find(n)}
    if not cart:
        st.info("Your cart is empty. Visit the Marketplace to add products.")
        st.button("Go to Marketplace", on_click=go, args=("Marketplace",))
        return
    for n, q in cart.items():
        p = find(n)
        c = st.columns([4, 1, 1, 1, 1.5, 1])
        c[0].markdown(f"**{p['emoji']} {n}**  \n₹{p['price']:,} each · stock {p['stock']}")
        c[1].button("➖", key=f"dec_{n}", on_click=change_qty, args=(n, -1))
        c[2].markdown(f"### {q}")
        c[3].button("➕", key=f"inc_{n}", on_click=change_qty, args=(n, 1))
        c[4].markdown(f"**₹{p['price'] * q:,}**")
        c[5].button("🗑️", key=f"rm_{n}", on_click=remove_item, args=(n,))
    st.divider()
    st.markdown(f"### Total: ₹{cart_total():,}")
    a, b = st.columns(2)
    a.button("Clear Cart", on_click=clear_cart, use_container_width=True)
    b.button("Demo Checkout ✅", on_click=checkout, use_container_width=True)


def page_doctor():
    st.header("🩺 Crop Doctor")
    st.caption("Educational demo only — no real AI or image recognition is used.")
    crop = st.selectbox("Select crop", list(CROPS))
    d = CROPS[crop]
    info_box(f"Example issue: {d['issue']}", f"<b>Symptoms:</b> {d['symptoms']}<br><b>Prevention:</b> {d['prevention']}")
    img = st.file_uploader("Upload a crop image", type=["jpg", "jpeg", "png"])
    if img is not None:
        try:
            st.image(img, caption="Uploaded image", width=350)
        except Exception:
            st.error("Could not display this image. Please upload a valid JPG or PNG.")
    if st.button("Check Sample Result"):
        if img is None:
            st.caption("No image uploaded — showing a predefined example.")
        st.warning(f"🧪 SIMULATED RESULT: Sample finding for {crop} — possible **{d['issue']}**. "
                   "This is a predefined demonstration, not a real diagnosis. "
                   "Please confirm suspected diseases with a qualified local agricultural expert.")


def page_guide():
    st.header("🌾 Madhya Pradesh Crop Guide")
    st.caption("Recommendations vary by district, weather, and soil-test results.")
    tabs = st.tabs(list(CROPS))
    for tab, (crop, d) in zip(tabs, CROPS.items()):
        with tab:
            info_box("Growing season", d["season"])
            info_box("General sowing period", d["sowing"])
            info_box("Soil requirements", d["soil"])
            info_box("Irrigation", d["irrigation"])
            info_box("Crop care tips", d["care"])


def page_fert():
    st.header("🧪 Fertilizer Knowledge Center")
    name = st.selectbox("Choose a fertilizer", list(FERTS))
    f = FERTS[name]
    info_box("Purpose", f["purpose"])
    info_box("General nutrients", f["nutrients"])
    info_box("Precautions", f["precautions"])
    info_box("Safe handling", f["handling"])
    st.info("Exact doses depend on crop, soil-test results and local conditions. Ask your agriculture officer or KVK.")


def stats_block():
    mine = [p for p in st.session_state.products if p["seller"] == "Demo Seller"]
    c = st.columns(3)
    c[0].metric("Your listings", len(mine))
    c[1].metric("Units in stock", sum(p["stock"] for p in mine))
    c[2].metric("Inventory value", f"₹{sum(p['price'] * p['stock'] for p in mine):,}")
    return mine


def page_login():
    st.header("🔐 Demo Login")
    role = st.session_state.role
    if role:
        st.success(f"Logged in as {role}.")
        if role == "Buyer":
            n = sum(st.session_state.cart.values())
            st.subheader("Buyer dashboard")
            st.metric("Items in cart", n)
            st.metric("Cart total", f"₹{cart_total():,}")
            st.button("Browse Marketplace", on_click=go, args=("Marketplace",))
        else:
            st.subheader("Seller dashboard summary")
            stats_block()
            st.button("Open Seller Dashboard", on_click=go, args=("Seller Dashboard",))
        if st.button("Logout"):
            st.session_state.role = None
            st.rerun()
        return
    st.caption("Demo credentials — Buyer: buyer / buyer123 · Seller: seller / seller123")
    r = st.radio("Role", list(USERS), horizontal=True)
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")
    if st.button("Login"):
        if (u.strip(), p) == USERS[r]:
            st.session_state.role = r
            st.rerun()
        else:
            st.error("Invalid username or password for the selected role.")


def page_seller():
    st.header("📦 Seller Dashboard")
    if st.session_state.role != "Seller":
        st.warning("This page is only for the Seller demo account. Please log in as seller.")
        st.button("Go to Login", on_click=go, args=("Login",))
        return
    mine = stats_block()
    st.subheader("List a new product")
    with st.form("add_product", clear_on_submit=True):
        name = st.text_input("Product name")
        cat = st.selectbox("Category", CATEGORIES)
        c1, c2 = st.columns(2)
        price = c1.number_input("Price (₹)", min_value=0.0, step=10.0)
        stock = c2.number_input("Stock", min_value=0, step=1)
        desc = st.text_area("Description")
        ok = st.form_submit_button("Add Product")
    if ok:
        if not name.strip() or not desc.strip():
            st.error("Name and description are required.")
        elif price <= 0:
            st.error("Price must be greater than zero.")
        elif stock <= 0:
            st.error("Stock must be at least 1.")
        elif find(name.strip()):
            st.error("A product with this name already exists.")
        else:
            emoji = {"Seeds": "🌱", "Fertilizers": "🧪", "Farming Tools": "🛠️", "Crop Protection": "🛡️"}[cat]
            st.session_state.products.append({"name": name.strip(), "category": cat, "price": int(price), "desc": desc.strip(),
                                              "seller": "Demo Seller", "stock": int(stock), "emoji": emoji})
            st.success("Product added! It now appears in the Marketplace.")
            st.rerun()
    st.subheader("Your listed products")
    st.dataframe([{"Product": p["name"], "Category": p["category"], "Price (₹)": p["price"], "Stock": p["stock"]}
                  for p in st.session_state.products if p["seller"] == "Demo Seller"], use_container_width=True)


def main():
    init_state()
    st.markdown(CSS, unsafe_allow_html=True)
    with st.sidebar:
        st.markdown("## 🌾 KrishiMart")
        st.caption("Your Trusted Partner in Smart Farming")
        st.radio("Navigate", PAGES, key="page")
        st.divider()
        st.caption(f"👤 {st.session_state.role or 'Not logged in'}")
        st.caption(f"🛒 Cart items: {sum(st.session_state.cart.values())}")
    {"Home": page_home, "Marketplace": page_market, "Shopping Cart": page_cart, "Crop Doctor": page_doctor,
     "MP Crop Guide": page_guide, "Fertilizer Knowledge Center": page_fert, "Login": page_login,
     "Seller Dashboard": page_seller}[st.session_state.page]()


main()
