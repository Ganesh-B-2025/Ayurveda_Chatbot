# Ayurveda Remedy Chatbot
This is a Flask-based web chatbot that suggests Ayurvedic remedies based on user-described symptoms using Natural Language Processing (NLP). It also handles basic greetings and farewells to create a more natural chat experience.

## Features
### unorder
* Accepts multiple comma-separated symptoms
* Returns the most relevant Ayurvedic remedies
* Uses TF-IDF and cosine similarity for intelligent symptom matching
* Simple, responsive, and elegant web-based chat UI
* Handles greetings and farewells naturally

## Tech Stack
### ounorder
* Backend: Flask, scikit-learn, pandas, numpy
* Frontend: HTML, CSS, vanilla JavaScript
* NLP: TF-IDF Vectorizer + Cosine Similarity

## Installation
### Order
1. Clone the repository:
> ```git clone https://github.com/Ganesh-B-2025/Ayurveda_Chatbot.git```
> ```cd ayurveda-chatbot```
2. Install dependencies:
> ```pip install -r requirements.txt```
3. Add your dataset: Place your dataset named ```ayurveda_remedies_extended.csv``` in the root directory. It >should contain the following columns:
>>```Disease/Symptoms```
>>```Remedy```
4. Run the application:
>```python app.py```
5. Visit in browser:
>Open http://127.0.0.1:5000/ in your browser.