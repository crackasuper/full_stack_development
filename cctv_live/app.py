from flask import Flask, render_template, Response
import cv2
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sql:///cctvlive.db"

camera = cv2.VideoCapture(0)

def cctv_live():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret,buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield(b'---frame\r\n'
                  b'Contetnt-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(cctv_live(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
    

