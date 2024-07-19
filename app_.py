from flask import Flask, render_template, request, send_from_directory
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img
import numpy as np
from gtts import gTTS
import subprocess
import os

template_folder = '/content/drive/MyDrive/Face_recognition_project/templates'
static_folder = '/content/drive/MyDrive/Face_recognition_project/static'

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

model = load_model('/content/drive/MyDrive/Face_recognition_project/hammad_recognition.h5')

celebrity_dict = {0: 'Not_hammad', 1: 'hammad'}
model.make_predict_function()

def generate_audio_message(text, audio_file):
    tts = gTTS(text=text, lang='en')
    tts.save(audio_file)

def predict_label(img_path):
    img = load_img(img_path, grayscale=True)
    img = img.resize((128, 128))
    img = np.array(img)
    img = img.reshape(128, 128, 1)
    img = img / 255.0
    pred = model.predict(img.reshape(1, 128, 128, 1))
    pred = np.argmax(pred.round(2))
    pred_celebrity = celebrity_dict[pred]

    if pred_celebrity == 'hammad':
        generate_audio_message("It is hammad.", "output.wav")

    if pred_celebrity == 'Not_hammad':
        generate_audio_message("It is not hammad.", "output.wav")

    return pred_celebrity

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index_.html")

@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_from_directory(static_folder, filename)

@app.route("/submit", methods=['POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']
        img_path = os.path.join(static_folder, img.filename)
        img.save(img_path)
        p = predict_label(img_path)
        if p == 'hammad':
            audio_path = "output.wav"
        else:
            audio_path = "output.wav"

    return render_template("index.html", celebrity=p, audio_path=audio_path, img_path=img_path)

if __name__ == '__main__':
    app.run()
