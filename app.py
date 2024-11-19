from flask import Flask, render_template, request, jsonify, redirect
import random
import string

app = Flask(__name__)

# Словарь для хранения коротких ссылок
url_mapping = {}

# Генерация случайного пути для короткой ссылки
def generate_short_link():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# API для создания короткой ссылки
@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.json
    original_url = data.get('url')
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400

    short_path = generate_short_link()
    url_mapping[short_path] = original_url

    return jsonify({'short_url': f'{request.host_url}{short_path}'})

# Перенаправление по короткой ссылке
@app.route('/<short_path>')
def redirect_to_url(short_path):
    original_url = url_mapping.get(short_path)
    if original_url:
        return redirect(original_url)
    return 'URL not found', 404

if __name__ == '__main__':
    app.run(debug=True)

