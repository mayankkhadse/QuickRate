# 🚀 QuickRate AI

<div align="center">

### Intelligent Inventory Management & AI-Powered Product Pricing System

An intelligent inventory management platform that helps businesses manage products, monitor stock, and instantly retrieve product pricing using AI-powered image recognition.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red?style=for-the-badge\&logo=streamlit)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge\&logo=sqlite)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-AI-green?style=for-the-badge)

</div>

---

## 📌 Overview

QuickRate AI is a smart inventory management application designed for retail businesses and shop owners. The platform combines traditional inventory management with Artificial Intelligence to provide intelligent pricing suggestions and image-based product identification.

The system enables staff and owners to efficiently manage inventory, monitor business performance, and quickly retrieve product information simply by uploading product images.

---

## ✨ Features

### 📦 Smart Inventory Management

* Add and manage products easily.
* Store product details including:

  * Product Name
  * Buying Price
  * Selling Price
  * Quantity
  * Branch Location
  * Product Image
* Automatic inventory storage using SQLite database.

### 🤖 AI Price Prediction

* Machine Learning-based selling price suggestions.
* Assists business owners in optimizing product pricing.
* Reduces manual effort and pricing inconsistencies.

### 📸 AI Product Scanner

* Upload product images directly from the dashboard.
* Automatically identifies matching products from inventory.
* Displays:

  * Product Name
  * Buying Price
  * Selling Price
  * Available Stock
  * Branch Information
  * Profit Analysis

### 📊 Business Intelligence Dashboard

* Total Products Overview
* Stock Monitoring
* Revenue Tracking
* Profit Margin Analysis
* Interactive Charts and Insights

---

## 🛠️ Tech Stack

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core Programming Language |
| Streamlit    | Frontend Framework        |
| SQLite       | Database Management       |
| Pandas       | Data Analysis             |
| NumPy        | Numerical Computation     |
| Scikit-Learn | Machine Learning          |
| Pillow       | Image Processing          |
| PyTorch      | AI Image Embeddings       |
| Git & GitHub | Version Control           |

---

## 📂 Project Structure

```bash
QuickRate/
│
├── app.py
├── requirements.txt
│
├── database/
│   ├── db.py
│   └── inventory.db
│
├── pages/
│   ├── dashboard.py
│   ├── inventory.py
│   ├── analytics.py
│   └── scan.py
│
├── services/
│   ├── inventory_service.py
│   ├── analytics_service.py
│   ├── ml_service.py
│   └── vision_service.py
│
├── uploads/
├── embeddings/
└── assets/
```

---

## 📸 Screenshots

### 📦 Inventory Management

#### Add Product Interface

![Inventory Screenshot 1](assets/inventory1.png)

#### Product Added Successfully

![Inventory Screenshot 2](assets/inventory2.png)

---

### 📸 AI Product Scanner

#### Upload Product Image

![Scanner Screenshot 1](assets/scanner1.png)

#### Product Recognition & Pricing Details

![Scanner Screenshot 2](assets/scanner2.png)

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/mayankkhadse/QuickRate.git
cd QuickRate
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🎯 Use Cases

* Retail Stores
* Electronics Shops
* Multi-Branch Businesses
* Small and Medium Enterprises
* Inventory Tracking Systems
* Smart Pricing Assistance

---

## 🔮 Future Improvements

* Barcode & QR Code Scanning
* Sales Forecasting
* Invoice Generation
* Cloud Database Integration
* Customer Analytics
* Low Stock Alerts

---

## 👨‍💻 Developer

**Mayank Khadse**

Passionate about Artificial Intelligence, Machine Learning, and building impactful software solutions.

---

<div align="center">

### ⭐ If you found this project useful, please consider giving it a star!

</div>
