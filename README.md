# fastapi-patient-api
FastAPI-based Patient Management System API with JSON data handling, sorting, and modular endpoints.
# 🏥 Patient Management System API (FastAPI)

This is a FastAPI-based backend project that provides APIs to manage patient records. It demonstrates REST API design, data handling using JSON, and query-based filtering/sorting.

---

## 🚀 Features

* 📌 View all patient records
* 📌 About endpoint describing the API
* 📌 Sort patients based on attributes (height, weight, BMI)
* 📌 Clean and modular FastAPI structure
* 📌 JSON-based data storage

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Language:** Python
* **Server:** Uvicorn
* **Data Storage:** JSON

---

## 📂 Project Structure

```
FASTAPI toutorial/
│── main.py
│── patients.json
│── requirements.txt
│── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2️⃣ Create virtual environment

```
python -m venv myenv
myenv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the server

```
uvicorn main:app --reload
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description       |
| ------ | -------- | ----------------- |
| GET    | `/`      | Welcome message   |
| GET    | `/about` | API description   |
| GET    | `/view`  | View all patients |
| GET    | `/sort`  | Sort patients     |

---

## 🔍 Example Query

```
http://127.0.0.1:8000/sort?sort_by=height&order=asc
```

---

## 📌 Future Improvements

* Add POST (create patient)
* Add DELETE/UPDATE APIs
* Connect database (SQLite/MongoDB)
* Add authentication

---

## 👨‍💻 Author

Rishabh Gupta

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
