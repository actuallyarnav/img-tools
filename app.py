from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from dotenv import load_dotenv

import os
import cv2
from werkzeug.utils import secure_filename
import imageops as imgop
load_dotenv()
UPLOAD_FOLDER='./static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1000 * 1000
app.secret_key =  os.getenv("SECRET_KEY")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("ERROR: Try uploading an image file", "warning")
            return redirect('/')
        file = request.files['file']
        if file.filename == '':
            flash("Please upload a valid image file", "warning")
            return redirect('/')
        if not allowed_file(file.filename):
            flash("Please upload a valid image file", "warning")
            return redirect('/')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('imageops', filename=filename))
    else:
        return render_template('index.html')


@app.route('/imageops/<filename>', methods=['POST', 'GET'])
def imageops(filename):
    return render_template('imageops.html', filename=filename)

@app.route('/rotate/<filename>', methods=['POST'])
def rotate(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    img = cv2.imread(path)

    if img is None:
       return "ERROR: image could not be loaded", 404
    direction = request.form.get('direction')

    if direction == 'clockwise':
        rotatedImg = imgop.imgRotateClockwise(img)

    elif direction == 'anticlockwise':
        rotatedImg = imgop.imgRotateCounterClockwise(img)

    else:
        return "ERROR: invalid direction", 400

    base_filename = os.path.basename(filename)

    if base_filename.startswith("rotated_"):
        base_filename = base_filename[len("rotated_"):]  # strip "rotated_"

    rotated_filename = f"rotated_{base_filename}"
    rotated_path = os.path.join(app.config['UPLOAD_FOLDER'], rotated_filename)

    cv2.imwrite(rotated_path, rotatedImg)

    return render_template('imageops.html', filename=rotated_filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
