import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

print("Loading dataset...")

df = pd.read_csv("EmotionDetection.csv")

X = df["text"]
y = df["Emotion"]

print("Training model...")

vectorizer = TfidfVectorizer(ngram_range=(1, 2))
X_vectorized = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=1000)
model.fit(X_vectorized, y)

joblib.dump(model, "emotion_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model and Vectorizer saved successfully ✅")
