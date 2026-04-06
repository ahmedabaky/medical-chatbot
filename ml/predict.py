import os
import joblib

# نفس فكرة path الصح
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# load model + vectorizer
model = joblib.load(os.path.join(CURRENT_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(CURRENT_DIR, "vectorizer.pkl"))


def predict_disease(text):
    text = text.lower().strip()
    text = text.replace(" _", "_")
    text = " ".join(text.split())

    X = vectorizer.transform([text])

    prediction = model.predict(X)

    return prediction[0]


if __name__ == "__main__":
    while True:
        user_input = input("Enter symptoms: ")
        result = predict_disease(user_input)
        print("Predicted Disease:", result)