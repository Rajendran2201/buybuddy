
#  BuyBuddy - Food Truck Restaurant Web App

BuyBuddy is a full-stack Django-based web application for a food truck-based restaurant that provides fast, healthy, and locally-sourced meals. With features like preorder, online ordering, cart management, and real-time location tracking, BuyBuddy brings convenience and transparency to your next bite!

---

## 🚀 Features

- 🧾 **Dynamic Menu:** Browse food items with images, descriptions, and prices.
- 🛒 **Cart System:** Add, remove, and update quantities in a real-time cart.
- 📦 **Order Options:** Choose between preorder, online order, or pickup.
- 📍 **Track Location:** View the current location of the food truck.
- 💳 **Checkout:** Payment gateway integration (coming soon).
- 📝 **Blog:** Behind-the-scenes stories of the food, sourcing, and team.
- 👥 **Customer Reviews:** View or submit reviews on dishes.
- 📷 **Gallery Page:** Visual journey of food and events.
- 📞 **Contact Page:** Reach out for private event bookings or inquiries.

---

## 🛠️ Tech Stack

### Backend
- **Python 3.11**
- **Django 5.1**
- **SQLite3** (default DB, can be swapped with PostgreSQL/MySQL)
- **Session-based cart management**

### Frontend
- **HTML5, CSS3**
- **Bootstrap 5** (or Tailwind optionally)
- **JavaScript / jQuery** for interactivity
- **FontAwesome** for icons

---


## 🛠️ Setup Instructions

### 🔧 Clone the Repository

```bash
git clone https://github.com/Rajendran2201/buybuddy.git
cd buybuddy
```

### 📦 Create a Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 🔑 Migrate and Run

```bash
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser to access BuyBuddy.

---

## 📈 Future Enhancements

- ✅ Payment Integration (Stripe/Razorpay)
- ✅ Order Tracking System
- ✅ Delivery Partner Module
- ✅ PWA for offline support
- ✅ Map-based location tracking (Google Maps API)

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements or suggestions.

---

## 📧 Contact

- **Email:** rajendran.stech@gmail.com

