# 🎭 Emotion Sentiment Analysis Web Application

---

# 🚀 Project Overview

This is a Flask-based Emotion Detection Web Application that allows users to:

- ✅ Register & Login  
- 📝 Submit Feedback  
- 🤖 Predict Emotion from Text using Machine Learning  
- 📊 View Emotion Analytics in Admin Dashboard  

The system integrates:
- Flask (Backend Framework)
- SQLite (Database)
- TF-IDF Vectorization
- Logistic Regression (Machine Learning Model)

---

# 🏗️ System Architecture

User  
↓  
Flask Web Application  
↓  
Machine Learning Model  
↓  
SQLite Database  
↓  
Admin Dashboard  

---

# 📂 Project Structure

emotion-analysis-app/  
│  
├── app1.py                # Main Flask Application  
├── train_model.py         # Model Training Script  
├── EmotionDetection.csv   # Dataset (Required)  
├── emotion_model.pkl      # Saved Trained Model  
├── vectorizer.pkl         # Saved TF-IDF Vectorizer  
├── database.db            # SQLite Database (Auto Created)  
└── README.md  

---

# 🧠 Machine Learning Model

## 🔹 Algorithm Used
- Logistic Regression

## 🔹 Text Processing
- TF-IDF Vectorizer (Unigram + Bigram)

## 🔹 Training Workflow

1. Load dataset (EmotionDetection.csv)  
2. Extract text and emotion labels  
3. Convert text into TF-IDF vectors  
4. Train Logistic Regression model  
5. Save:
   - emotion_model.pkl  
   - vectorizer.pkl  

## ▶️ Train the Model

python train_model.py

---

# 🌐 Web Application Features

---

## 🏠 Home Page

Navigation links:
- Signup  
- Signin  
- Give Feedback  
- Admin  

---

## 👤 User Signup

- Stores new user in SQLite database  
- Prevents duplicate usernames  

---

## 🔐 User Signin

- Validates username and password  
- Returns success or error message  

---

## 📝 Feedback Submission

User provides:
- Username  
- Rating  
- Comment  

System:
- Validates user  
- Predicts emotion using ML model  
- Stores:
  - Username  
  - Rating  
  - Comment  
  - Predicted Emotion  

---

## 📊 Admin Dashboard

### 🔑 Admin Credentials

Username: admin  
Password: admin123  

### Admin Can View:

- All feedback entries  
- Emotion-wise summary count  

Example Output:

{
  "feedback_data": [...],
  "emotion_summary": {
    "happy": 10,
    "sad": 5,
    "angry": 2
  }
}

---

# 🗄️ Database Details

- Database: SQLite  
- File: database.db  
- Automatically created on first run  

## Tables

### User Table
- id  
- username  
- password  

### Feedback Table
- id  
- username  
- rating  
- comment  
- emotion  

---

# 🛠️ Installation & Setup

---

## 1️⃣ Clone Repository

git clone https://github.com/Vaishnav-M01/Emotion-Detection-

---

## 2️⃣ Create Virtual Environment (Recommended)

Windows:

python -m venv venv  
venv\Scripts\activate  

---

## 3️⃣ Install Required Packages

pip install flask flask_sqlalchemy pandas scikit-learn joblib  

---

## 4️⃣ Train Machine Learning Model

python train_model.py  

---

## 5️⃣ Run Flask Application

python app1.py  

Application runs at:

http://127.0.0.1:5000/

---

# 📊 Technology Stack

Backend: Flask  
Database: SQLite  
ML Model: Logistic Regression  
Text Processing: TF-IDF  
Model Storage: Joblib  

---

# 👨‍💻 Author

Vaishnav M  
Aspiring AI Engineer | Data Science Enthusiast  

---
