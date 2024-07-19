from flask import Flask, render_template, request
import cv2
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img

app = Flask(__name__)

model = load_model('hammad_recognition.h5')
celebrity_dict = {0: 'Not_hammad', 1: 'hammad'}
model.make_predict_function()

# Initialize the webcam
cap = cv2.VideoCapture(0)

def predict_label(img):
    img = cv2.resize(img, (128, 128))
    img = img.reshape(128, 128, 1)
    img = img / 255.0
    pred = model.predict(img.reshape(1, 128, 128, 1))
    pred = np.argmax(pred.round(2))
    pred_celebrity = celebrity_dict[pred]
    return pred_celebrity

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def get_output():
    if request.method == 'POST':
        _, frame = cap.read()
        img_path = "static/live_image.jpg"
        cv2.imwrite(img_path, frame)
        p = predict_label(frame)
        return render_template("index.html", celebrity=p, img_path=img_path)

if __name__ == '__main__':
    app.run(debug=True)
