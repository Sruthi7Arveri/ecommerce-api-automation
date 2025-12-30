# API Automation Framework

## 📌 Project Overview
This project is a basic API automation framework built using **Python**, **pytest**, and the **requests** library.  
It is designed to validate REST APIs by covering positive and negative test scenarios in a clean and reusable structure.

---

## 🛠️ Tech Stack
- Python
- Pytest
- Requests
- Pytest-HTML (for reporting)

---

## 📂 Framework Structure

api-automation-framework/
│
├── config/  
│   └── config.py              # Environment configurations (Base URL)
│
├── utils/  
│   └── api_client.py          # Reusable API client methods
│
├── tests/  
│   ├── test_products.py       # Product API test cases  
│   ├── test_cart.py           # Cart API test cases  
│   └── test_cart_negative.py  # Negative scenarios  
│
├── reports/  
│   └── api_report.html        # HTML execution report  
│
├── conftest.py                # Pytest fixtures
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation


## Install dependencies
- pip install -r requirements.txt

## Run all tests
- pytest -v

## Generate HTML report
- pytest -v --html=reports/api_report.html --self-contained-html

## 📌 Future Enhancements

- Authentication handling
- Header management
- Logging support
- CI/CD integration