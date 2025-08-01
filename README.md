# Court-Data Fetcher & Mini Dashboard

A simple Flask-based web app to fetch Indian court case metadata based on case type, number, and filing year.

---

## ✅ Features
- Input: Case Type, Case Number, Filing Year
- Output: Parties' names, Filing date, Next hearing date, Latest order PDF link
- Scraping using Selenium
- Logs each query and response in SQLite
- Clean UI with HTML/CSS
- Error handling for invalid inputs

---

## 🏛️ Target Court
- Faridabad District Court (https://districts.ecourts.gov.in/faridabad)

---

## 🛠️ Tech Stack
- Python 3.10+
- Flask
- Selenium (headless)
- SQLite

---

## 🚀 Setup Instructions

1. Clone the repo
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate

## Install dependencies

    pip install -r requirements.txt

## Run the app

    python app.py
