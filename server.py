from flask import Flask, render_template, request
import os

app = Flask(__name__)

pth=os.path.join('Static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['POST'])
def analyze_survey():
    # Implement your survey analysis logic here
    # Access survey data using request.form
    return "Survey analysis result"

@app.route('/text', methods=['POST'])
def analyze_text():
    text_input = request.form['text_input']
    # Implement your text analysis logic here
    return f"Text analysis result for: {text_input}"

@app.route('/audio', methods=['POST'])
def analyze_audio():
    # Implement your audio analysis logic here
    # Access audio file using request.files['audio_file']
    return "Audio analysis result"

if __name__ == '__main__':
    app.run(debug=True)
