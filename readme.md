# Ayurveda Remedy Chatbot
<p>This is a Flask-based web chatbot that suggests Ayurvedic remedies based on user-described symptoms using Natural Language Processing (NLP). It also handles basic greetings and farewells to create a more natural chat experience.</p>

<h2>Features</h2>
<ul style="list-style-type:circle">
    <li>Accepts multiple comma-separated symptoms</li>
    <li>Returns the most relevant Ayurvedic remedies</li>
    <li>Uses TF-IDF and cosine similarity for intelligent symptom matching</li>
    <li>Simple, responsive, and elegant web-based chat UI</li>
    <li>Handles greetings and farewells naturally</li>
</ul>

<h2>Tech Stack</h2>
<ul>
<li>Backend: Flask, scikit-learn, pandas, numpy</li>
<li>Frontend: HTML, CSS, vanilla JavaScript</li>
<li>NLP: TF-IDF Vectorizer + Cosine Similarity</li>
</ul>

<h2>Installation</h2>
    <ol style="1">
        <li>Clone the repository:</li>
        <ul style="list-style-type:none">
            <li>git clone https://github.com/Ganesh-B-2025/Ayurveda_Chatbot.git</li>
            <li>cd ayurveda-chatbot</li>
        </ul>
        <li>Install dependencies:</li>
        <ul style="list-style-type:none">
            <li>pip install -r requirements.txt</li>
        </ul>  
        <li>Add your dataset: Place your dataset named ayurveda_remedies_extended.csv in the root directory.
            It should contain the following columns:</li>
        <ul style="list-style-type:none">
            <li>Disease/Symptoms</li>
            <li>Remedy</li>
        </ul>
        <li>Run the application:</li>
        <ul style="list-style-type:none">
            <li>python app.py</li>
        </ul>
        <li>Visit in browser:</li>
        <ul style="list-style-type:none">
            <li>Open http://127.0.0.1:5000/ in your browser.</li>
        </ul>
    </ol>

<h2>📁 Folder Structure</h2>
<ul style="list-style-type:none">
    <li>ayurveda-chatbot</li>
    <ul>
        <p>data</p>
        <ul style="list-style-type:none">
            <li>ayurveda_remedies_extended.csv</li>
        </ul>
        <p>static</p>
        <ul style="list-style-type:none">
            <li>style.css</li>
        </ul>
        <p>templates</p>
        <ul style="list-style-type:none">
            <li>index.html</li>
        </ul>
    </ul>
    <li>app.py</li>
</ul>


