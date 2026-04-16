# hotel-review-ml-vf

Progetto di Machine Learning per l'analisi automatica delle recensioni nel settore hospitality.

## Descrizione

Il sistema permette di:
- classificare le recensioni per reparto (Housekeeping, Reception, F&B)
- analizzare il sentiment (positivo/negativo)

Il progetto include dataset, pipeline di Machine Learning e una semplice dashboard.

---

## Installazione

Installare le dipendenze:

pip install -r requirements.txt

---

## Generazione dataset

cd src
python generate_dataset.py

Il dataset verrà salvato nella cartella data/.

---

## Training modello

python train_model.py

---

## Avvio dashboard

streamlit run app.py

---

## Struttura del progetto

hotel-review-ml/
│
├── data/
├── models/
├── src/
├── requirements.txt
└── README.md

---

## Note

Il dataset utilizzato è sintetico ed è stato creato a scopo didattico.
