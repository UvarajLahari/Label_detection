from flask import *  
import io
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'My Project 84767-aedc1255c92f.json'
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        with open("img.jpg","wb") as image_f:
            image_f.write(f.read())
        with io.open("img.jpg", 'rb') as image_file:
            content = image_file.read()
        # content = f.read()
        client = vision.ImageAnnotatorClient()
        image = vision.types.Image(content=content)

        response = client.label_detection(image=image)
        labels = response.label_annotations
        print('Labels:')
        print(response)
        print(labels)
        labels_detect=[]
        for label in labels:
            labels_detect.append((label.description))
        print(labels_detect)
        f.save(f.filename)
        return render_template("file_upload_form.html", name = labels_detect)  
  
if __name__ == '__main__':  
    app.run(debug = True)  
