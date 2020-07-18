from flask import Flask, render_template, send_file
import os
from .main.controller.generate import gen_pdf
app = Flask(__name__, template_folder='./main/view/templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download-pdf', methods=['POST'])
def download_cert():
    gen_pdf()
    # return render_template('index.html')
    path = "./main/view/static/downloads/out.pdf"
    return send_file(path, as_attachment=True)
