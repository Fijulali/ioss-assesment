from flask import Flask, render_template, request, redirect
import random, string
import os

app = Flask(__name__)

url_map = {}  # short_code -> original_url

def generate_short_code(length=5):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_code = generate_short_code()
        url_map[short_code] = long_url
        short_url = request.host_url + short_code
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_url(short_code):
    long_url = url_map.get(short_code)
    if long_url:
        return redirect(long_url)
    return "URL not found", 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


