# DistilBERT CyberSec URL Detector

This project detects malicious or unsafe URLs using a fine-tuned DistilBERT model.
The frontend is built using HTML, CSS, and JavaScript, and the backend is hosted on Hugging Face Spaces.

---

## Model
The trained DistilBERT model is hosted here:
https://huggingface.co/Crystlfly/DistilBERT-CyberSec-Detector

---

## Backend (Hugging Face Space)
Backend API is hosted on Hugging Face Spaces:
https://huggingface.co/spaces/Crystlfly/CyberSec-API

Backend source files:
- app.py
- requirements.txt
- Dockerfile

---

## Frontend
The frontend calls the backend API using fetch():

fetch("https://crystlfly-cybersec-api.hf.space/analyze", { ... })

---

## 📂 Project Structure

project/
│── frontend/
│     ├── index.html
│     ├── style.css
│     └── script.js
│
│── backend/
│     ├── app.py
│     ├── requirements.txt
│     └── Dockerfile
│
└── README.md

---

## How to Run Locally

### Install backend dependencies:
pip install -r backend/requirements.txt

### Start backend:
python backend/app.py

### Open frontend:
Open `index.html` in your browser.

---

## 🤝 Contributions
PRs are welcome!
