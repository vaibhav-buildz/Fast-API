# 🚀 FastAPI Learning & Hands-On Practice

This repository contains hands-on code examples and CRUD operations built while following the **Complete FastAPI Course** tutorial series by **TechSimPlus / Pratik Misra**.

> 📚 **Course Resource**: [Complete FastAPI Course Playlist on YouTube](https://www.youtube.com/watch?v=tMJA41xhBZM&list=PLUhY5ME1VdIumaSa-m5SQ-ztTL8NWY8Gh)

---

## 📌 Features & Topics Covered

- 🌐 **Basic Routes**: GET endpoints returning JSON responses.
- 🔍 **Path Parameters**: Fetching specific items by ID (`/product/{product_id}`).
- ❓ **Query Parameters**: Reading query parameters from the request (`/greet?name=John&age=25`).
- 📝 **Data Validation with Pydantic (DTOs)**: Using `ProductDTO` model for request body validation.
- ⚡ **Full CRUD Operations**:
  - `GET /products` - Get list of products
  - `GET /product/{product_id}` - Get product by ID
  - `POST /create_product` - Add a new product
  - `PUT /update_product/{product_id}` - Update existing product
  - `DELETE /delete_product/{product_id}` - Delete product

---

## 📁 Project Structure

```text
Fast-API/
├── dtos.py         # Pydantic schema model (ProductDTO)
├── main.py         # FastAPI application entry point & route definitions
├── mockData.py     # In-memory mock product dataset
├── .gitignore      # Git ignore configuration
└── README.md       # Project documentation
```

---

## 🛠️ Getting Started

### 1. Prerequisites
- Python 3.10+ installed

### 2. Set Up Virtual Environment

```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On Windows:
.\env\Scripts\activate

# On macOS/Linux:
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn pydantic
```

---

## 🏃 Running the FastAPI Server

Start the development server with live reloading enabled:

```bash
uvicorn main:app --reload
```

The server will start running at: **`http://127.0.0.1:8000`**

---

## 📖 Interactive API Documentation

FastAPI provides automatic, interactive API documentation out of the box:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🙏 Acknowledgements

Special thanks to **TechSimPlus / Pratik Misra** for the insightful [FastAPI Tutorial Series](https://www.youtube.com/watch?v=tMJA41xhBZM&list=PLUhY5ME1VdIumaSa-m5SQ-ztTL8NWY8Gh).
