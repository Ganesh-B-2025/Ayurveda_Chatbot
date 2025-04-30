# Ayurveda Remedy Chatbot
This is a Flask-based web chatbot that suggests Ayurvedic remedies based on user-described symptoms using Natural Language Processing (NLP). It also handles basic greetings and farewells to create a more natural chat experience.

### unorder
* Accepts multiple comma-separated symptoms
* Returns the most relevant Ayurvedic remedies
* Uses TF-IDF and cosine similarity for intelligent symptom matching
* Simple, responsive, and elegant web-based chat UI
* Handles greetings and farewells naturally

### Tech Stack
* Backend: Flask, scikit-learn, pandas, numpy
* Frontend: HTML, CSS, vanilla JavaScript
* NLP: TF-IDF Vectorizer + Cosine Similarity

### Installation
1. Clone the repository:
>```git clone https://github.com/Ganesh-B-2025/Ayurveda_Chatbot.git```
>```cd ayurveda-chatbot```
2. Install dependencies:
>```pip install -r requirements.txt```
3. Add your dataset: Place your dataset named ```ayurveda_remedies_extended.csv``` in the root directory. It >should contain the following columns:
>```Disease/Symptoms```<br>
>```Remedy```
4. Run the application:
>```python app.py```
5. Visit in browser:
>Open http://127.0.0.1:5000/ in your browser.

## 📁 Folder Structure  
### Ayurveda_Chatbot  
├── `data/`  <br>
│   └── `ayurveda_remedies_extended.csv`  <br>
├── `static/`  <br>
│   └── `style.css`  <br>
├── `templates/`  <br>
│   └── `index.html`  <br>
├── `app.py`  <br>
└── `requirements.txt`  <br>

## Example Inputs <br>
```headache```<br>
```cold```<br>
```anxiety```<br>
```hi / bye```<br>

## To-Do (Optional)
1. Add user authentication
2. Integrate with a database (e.g., MongoDB)
3. Export recommendations to PDF
4. Add voice input and response

## 🤝 Contributing
Feel free to fork and improve this project. Pull requests are welcome!

## License
This project is open-source and free to use under the MIT License.

