from flask import Flask, request, redirect, render_template, url_for
import string
import random

app = Flask(__name__)

# In-memory database to store shortened URLs
url_mapping = {}

# Function to generate a random string of fixed length
def generate_short_id(num_chars=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_id = generate_short_id()
        url_mapping[short_id] = original_url
        return render_template('index.html', short_url=url_for('redirect_to_url', short_id=short_id, _external=True))
    return render_template('index.html')

@app.route('/<short_id>')
def redirect_to_url(short_id):
    original_url = url_mapping.get(short_id)
    if original_url:
        return redirect(original_url)
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')