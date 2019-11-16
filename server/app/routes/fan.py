from flask import render_template, request, url_for, flash, jsonify, redirect, abort
import time

# from app.models.fan import Fan
from app import app, db

# 노말 모드
@app.route('/normal', methods=["GET", "POST"])
def normal():

    return render_template('normal.html')

# 센서 인식모드
# @app.route('/sensor')
# def sensor():
#     return render_template('sensor.html')


# 얼굴인식 모드
# @app.route('/face')
# def face():
#     return render_template('face.html')
