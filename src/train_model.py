import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
from preprocess import preprocess

# Carica dataset
df = pd.read_csv("../data/reviews_dataset.csv")

# Preprocessing
df["text"] = df["text"].apply(preprocess)

# Features e target
X = df["text"]
y_dep = df["department"]
y_sent = df["sentiment"]

# Vettorizzazione
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Split
X_train, X_test, y_dep_train, y_dep_test = train_test_split(X_vec, y_dep, test_size=0.2)

_, _, y_sent_train, y_sent_test = train_test_split(X_vec, y_sent, test_size=0.2)

# Modelli
dep_model = LogisticRegression()
dep_model.fit(X_train, y_dep_train)

sent_model = LogisticRegression()
sent_model.fit(X_train, y_sent_train)

# Salvataggio
with open("../models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("../models/dep_model.pkl", "wb") as f:
    pickle.dump(dep_model, f)

with open("../models/sent_model.pkl", "wb") as f:
    pickle.dump(sent_model, f)

print("Modelli addestrati e salvati!")
