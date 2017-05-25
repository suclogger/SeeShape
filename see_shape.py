from flask import Flask, request
from datetime import datetime
from label_image import Predict,judge_shape
from PIL import Image


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/see_shape',methods=['GET','POST'])
def GetNoteText():
    if request.method == 'POST':
        file = request.files['file']
        # filename = file.filename
        # filePath = '/tmp/' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.png'
        filePath = '/tmp/' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'
        file.save(filePath)
        # im = Image.open(filePath)
        # im.save(filePath.replace("png", 'jpg'), "JPEG", quality=10)
        # predictResult = judge_shape(filePath.replace("png", 'jpg'))
        predictResult = judge_shape(filePath)
        return str(predictResult[0])
    else:
        return "Y U NO USE POST?"

if __name__ == '__main__':
    app.run(host= '0.0.0.0')