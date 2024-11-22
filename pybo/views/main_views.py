from flask import Blueprint
from flask import Blueprint, request, redirect, url_for, render_template, jsonify
import os
import base64

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello Pybo!'

@bp.route('/')
def index():
    return 'Pybo index'

@bp.route('/uploadfile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join('uploads', filename))
            return redirect(url_for('main.upload_file'))
    return render_template('upload.html')

@bp.route('/draw', methods=['GET'])
def draw():
    return render_template('draw.html')

image_number = 1
@bp.route('/upload', methods=['POST'])
def upload_image():
    global image_number
    data = request.get_json()
    image_data = data['image'].split(',')[1]
    image_data = base64.b64decode(image_data)
    filename = f'uploaded_image{image_number}.png'
    filepath = os.path.join('uploads', filename)
    with open(filepath, 'wb') as f:
        f.write(image_data)
    image_number += 1
    return jsonify({'message': '이미지 업로드 완료!'})
