from flask import render_template, request, url_for, flash, jsonify, redirect, abort, Response
import face_recog

from app import app, db
from app.models.fan import Fan

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def gen(file):
    while True:
        jpg_bytes = file.get_jpg_bytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(
        gen(face_recog.FaceRecog()),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


@app.route('/face/save', methods=["GET", "POST"])
def face_save():
    if request.method == "POST":
        file = request.form['file']
        time = request.form['time']

    return render_template('fan/face.html')


@app.route('/face/select', methods=["GET", "POST"])
def face_select():
    return render_template('fan/cam.html')


@app.route('/face/uplaod', methods=["GET", "POST"])
def face_upload():
    if request.method == 'POST':
        file = request.form['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))

    return render_template('fan/cam.html')
