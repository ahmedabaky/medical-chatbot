#  Medical Chatbot (AI + NLP)

An intelligent medical chatbot that predicts possible diseases based on user symptoms using Natural Language Processing (NLP) and Machine Learning.

---

##  Project Overview

This project is an AI-powered medical assistant that takes user-input symptoms in text form and predicts the most likely disease.

It is designed to demonstrate how AI can assist in healthcare by providing quick preliminary analysis.

---

##  Features

*  Predict diseases based on symptoms
*  Text preprocessing using NLP techniques
*  Machine Learning model for classification
*  Fast and lightweight system
*  API-ready using FastAPI (optional)

---

##  Technologies Used

* Python
* Scikit-learn
* Pandas & NumPy
* NLP (TF-IDF, preprocessing)
* FastAPI (for deployment)

---

##  Project Structure

```
medical-chatbot/
│
├── app/                # FastAPI application
├── ml/                 # Machine Learning logic
│   ├── train.py
│   ├── predict.py
│   ├── preprocessing.py
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/ahmedabaky/medical-chatbot.git
cd medical-chatbot
```

### 2. Create virtual environment

```
python -m venv venv
```

### 3. Activate environment

**Windows (PowerShell):**

```
venv\Scripts\activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

---

##  How to Run

### Option 1: Run the model directly

```
python ml/predict.py
```

---

### Option 2: Run API (Recommended 🚀)

```
uvicorn app.main:app --reload
```

Then open:

```
http://127.0.0.1:8000/docs
```

---

##  Example Input

```
I have fever and headache
```

##  Output

```
Predicted Disease: Flu
```

---

##  Model Details

* Vectorization: TF-IDF
* Model: Machine Learning Classifier
* Input: Free text symptoms
* Output: Predicted disease label

---

##  Future Improvements

* Improve model accuracy
* Add deep learning models
* Build a full web/mobile interface
* Connect with real medical datasets

---

##  Disclaimer

This project is for educational purposes only and should not be used for real medical diagnosis.

---

##  Author

Ahmed Abdelbaky
AI Engineer (in progress )
