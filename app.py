from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load and preprocess dataset
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    df.dropna(inplace=True)
    df['Disease/Symptoms'] = df['Disease/Symptoms'].str.lower().str.strip()
    df['Remedy'] = df['Remedy'].str.lower().str.strip()
    return df

# Train TF-IDF model
def train_tfidf_model(df):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['Disease/Symptoms'])
    return vectorizer, tfidf_matrix

# Handle greetings and farewells
def check_greetings_or_farewells(query):
    greetings = ["hello", "hi", "hey", "greetings"]
    farewells = ["bye", "goodbye", "exit", "see you", "farewell"]

    query_lower = query.lower().strip()
    if query_lower in greetings:
        return "Hello! How can I assist you with Ayurveda remedies today?"
    elif query_lower in farewells:
        return "Goodbye! Stay healthy and take care. 😊"
    return None

# Find remedies for multiple symptoms
def find_best_match(query, df, vectorizer, tfidf_matrix):
    query_check = check_greetings_or_farewells(query)
    if query_check:
        # Return greeting/farewell response
        return [query_check]

    symptoms = [symptom.strip().lower() for symptom in query.split(',')]  # Process comma-separated input
    remedies = set()

    for symptom in symptoms:
        query_vector = vectorizer.transform([symptom])
        similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
        
        top_n = 3
        top_indices = np.argsort(similarities)[-top_n:][::-1]
        found_remedies = [df.iloc[i]['Remedy'] for i in top_indices if similarities[i] > 0.1]
        
        remedies.update(found_remedies)

    return list(remedies) if remedies else ["No relevant remedy found."]

# Load dataset and train model
df = load_dataset(r"data/ayurveda_remedies_extended.csv")
vectorizer, tfidf_matrix = train_tfidf_model(df)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get_remedy', methods=['POST'])
def get_remedy():
    data = request.json
    query = data.get("query", "")
    remedies = find_best_match(query, df, vectorizer, tfidf_matrix)
    
    return jsonify({"remedy": ', '.join(remedies)})

if __name__ == '__main__':
    app.run(debug=True)
