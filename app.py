from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    input_text = data['input']
    mode = data['mode']
    
    if mode == 'Latin':
        command = ['bin/words', input_text]
    else:  # English mode
        command = ['bin/words', '~E', input_text]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = f"Error: {e.stderr}"
    
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)