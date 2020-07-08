#ignore tensorflow warnings
import warnings
warnings.filterwarnings("ignore")
from os import environ, chdir
environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

#Libraries needed 
from flask import Flask, request, render_template
import tensorflow as tf
from keras.models import Sequential, load_model
import numpy as np
from keras.preprocessing import image
import boto3
from botocore.exceptions import NoCredentialsError
import mysql.connector

#Mysql connection
mydb = mysql.connector.connect(
  host="mysql2020.c8zaxnpj5b57.us-east-1.rds.amazonaws.com",
  user="mysql2020",
  passwd="mysql2020",
  database="cloudcruise"
)

def classify(image, model):
    preds = model.predict(image)
    #print("Prediction is ",preds)
    if preds>=0.2:
        classification='Rotten fruit'
    else:
        classification='Fresh fruit'
    
    print("Classification-",classification)
    return classification

app = Flask(__name__)

#Declare this as global:
global model
global graph
graph = tf.get_default_graph()

@app.route('/')
def entry_page():
    #Jinja template of the webpage
    return render_template('index.html')

@app.route('/predict_object/', methods=['GET', 'POST'])
def render_message():
    with graph.as_default():
        
        #Loading CNN model
        model = load_model('FruitStatus_cnn_0.99.h5')
            
        try:
            #Get image URL as input
            image_url = request.form['image_url']
            print("image_url is:",image_url)
            
            #Apply same preprocessing used while training CNN model
            test_image = image.load_img(image_url,target_size =(64,64,3))
            test_image = image.img_to_array(test_image)
            test_image = test_image/255
            test_image = np.expand_dims(test_image, axis = 0)
            pred_class = classify(test_image, model)

            #Print model prediction for debugging purpose
            print(pred_class)
           
            #Store model prediction results to pass to the web page
            message = "Model prediction: {}".format(pred_class)
            print('Python module executed successfully')

            #Insert the record into logs table 
            mycursor = mydb.cursor()
            sql = "INSERT INTO logs (image_name, image_class) VALUES (%s, %s)"
            val = (image_url, pred_class)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            #Store error to pass to the web page
            message = "Error encountered. Try another image. ErrorClass: {}, Argument: {} and Traceback details are {}".format(e.__class__,e.args,e.__doc__)
        
        s3 = boto3.client('s3')
        s3filename='_'.join(pred_class.split(" ")) + '.jpg'
        s3.upload_file(image_url, 'cloudcruise', s3filename)
            
    #Return the model results to the web page
    return render_template('index.html',
                        message=message,
                        image_url=image_url)

#Debug is disabled for running in a jupyter notebook
#app.run(debug=False)
app.run(host="0.0.0.0", port=80)
