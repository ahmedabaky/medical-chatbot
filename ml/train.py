from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os


from preprocessing import load_and_preprocess_data

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(CURRENT_DIR, "data", "dataset.csv")
print("DATA PATH:", data_path)   


X, y = load_and_preprocess_data(data_path)

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vec , y)

joblib.dump(model, os.path.join(CURRENT_DIR, "model.pkl"))
joblib.dump(vectorizer, os.path.join(CURRENT_DIR, "vectorizer.pkl"))

print("Model trained successfully")
