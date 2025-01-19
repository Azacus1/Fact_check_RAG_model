from flask import Flask, render_template, request
from model.generate_response import generate_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    query = request.form['query']
    response = generate_response(query)
    return render_template('result.html', response=response)

if __name__ == "__main__":
    app.run(debug=True)
