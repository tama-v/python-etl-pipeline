# 🚀 Python ETL Pipeline

A modular ETL (Extract, Transform, Load) pipeline built with Python following Data Engineering best practices.

This project demonstrates how to build a clean, maintainable, and testable ETL application using Pandas, PostgreSQL, SQLAlchemy, and Pytest.

---

## ✨ Features

- Modular ETL architecture
- Configuration using environment variables
- Centralized logging
- PostgreSQL integration with SQLAlchemy
- Unit testing with Pytest
- Mocking database operations
- Code coverage support
- Professional project structure

---

## 📂 Project Structure

```
python-etl/

├── app/
│   ├── config/
│   ├── extract/
│   ├── load/
│   ├── transform/
│   ├── utils/
│   └── main.py
│
├── data/
│   └── mahasiswa.csv
│
├── logs/
│
├── tests/
│   ├── test_extract.py
│   ├── test_load.py
│   ├── test_path.py
│   └── test_transform.py
│
├── requirements.txt
├── .env.example
└── README.md
```

---

# 🛠 Technologies

- Python 3.14
- Pandas
- SQLAlchemy
- PostgreSQL
- python-dotenv
- Pytest
- Pytest-Cov

---

# ⚙ Installation

Clone repository

```bash
git clone https://github.com/yourusername/python-etl.git
```

Move into project

```bash
cd python-etl
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Copy

```bash
cp .env.example .env
```

Edit

```
DATABASE_HOST=
DATABASE_PORT=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
```

---

# ▶ Run ETL

```bash
python -m app.main
```

---

# 🧪 Run Tests

```bash
python -m pytest -v
```

---

# 📊 Coverage

```bash
python -m pytest --cov=app
```

Generate HTML report

```bash
python -m pytest --cov=app --cov-report=html
```

---

# 📖 Learning Objectives

This repository is created as part of a Data Engineering learning journey covering:

- Python Best Practices
- ETL Development
- SQLAlchemy
- Logging
- Environment Configuration
- Unit Testing
- Mocking
- Code Coverage
- CI/CD (Upcoming)
- Docker (Upcoming)
- Apache Airflow (Upcoming)

---



<!-- ===== -->
- Git Workflow Practice
<!-- ======= -->
## Docker Learning

This branch is used to practice Git branching.


# 📜 License

MIT License