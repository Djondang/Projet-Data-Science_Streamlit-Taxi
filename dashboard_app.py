import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement du modèle et des données
rf_model = joblib.load("random_forest_model.pkl")
# df = pd.read_csv("df_cleaned.csv")  # ou utiliser un échantillon pour les visualisations

st.title("NYC Taxi Fare Estimator")

# Section 1 : Formulaire interactif de prédiction
st.header("Estimer le prix d'une course")

trip_distance = st.slider("Distance du trajet (miles)", 0.1, 30.0, 2.0, step=0.1)
trip_duration = st.slider("Durée du trajet (minutes)", 1, 120, 10)
pickup_hour = st.slider("Heure de prise en charge", 0, 23, 14)
pickup_dayofweek = st.selectbox("Jour de la semaine", ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"])
passenger_count = st.number_input("Nombre de passagers", 1, 6, value=1)

# Mapping jour chiffre
jour_to_int = {"Lundi": 0, "Mardi": 1, "Mercredi": 2, "Jeudi": 3, "Vendredi": 4, "Samedi": 5, "Dimanche": 6}
pickup_dayofweek = jour_to_int[pickup_dayofweek]

# Prédiction
if st.button("Prédire le tarif"):
    X_input = pd.DataFrame({
        "trip_distance": [trip_distance],
        "trip_duration_min": [trip_duration],
        "pickup_hour": [pickup_hour],
        "pickup_dayofweek": [pickup_dayofweek],
        "passenger_count": [passenger_count]
    })
    fare_pred = rf_model.predict(X_input)[0]
    st.success(f"💰 Tarif estimé : {fare_pred:.2f} $")

# Section 2 : Visualisation rapide
st.header("📊 Aperçu des analyses (EDA)")
