import streamlit as st
import pickle
from preprocess import preprocess

# Caricamento modelli
vectorizer = pickle.load(open("../models/vectorizer.pkl", "rb"))
dep_model = pickle.load(open("../models/dep_model.pkl", "rb"))
sent_model = pickle.load(open("../models/sent_model.pkl", "rb"))

st.title("Hotel Review Analyzer")

review = st.text_area("Inserisci una recensione")

if st.button("Analizza"):
    text = preprocess(review)
    vec = vectorizer.transform([text])

    dep = dep_model.predict(vec)[0]
    sent = sent_model.predict(vec)[0]

    st.subheader("Risultato")
    st.write("Reparto:", dep)
    st.write("Sentiment:", sent)
