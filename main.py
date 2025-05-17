from flask import Flask, render_template, request
from utils.process_sped import process_sped_file

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['txtFile']
        process_sped_file(file)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)