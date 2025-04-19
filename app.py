from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/")
def index():
    return "Serveur Astronaut Scraper actif !"

@app.route("/predict")
def predict():
    # Simule une prédiction (+2 ou -2) basée sur une logique simple
    prediction = random.choice(["+2", "-2"])
    return jsonify({"prediction": prediction})
