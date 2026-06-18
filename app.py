from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Simple API endpoint
@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello, World!"})

# Form submission example
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', 'Anonymous')
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
