from flask import Flask,request,jsonify,render_template
from joblib import load
import pandas as pd
import datetime
import os

app = Flask(__name__)
#model_path = os.getcwd()+r'\sentimentanalysis\models\model'
model_path = r'C:/Users/mrpra/sentiment Analysis for Movies Reviews and Translation/sentimentanalysis/models/model'
model_file = os.path.join(model_path, 'classifier.pkl')

# Check validity
if os.path.exists(model_file):
    print("File exists, size:", os.path.getsize(model_file))
    try:
        classifier = load(model_file)
        
        print("Model loaded successfully.")
    except Exception as e:
        print("Error loading model:", e)
else:
    print("Model file does not exist at:", model_file)


def predictfunc(review):    
      
     prediction = classifier.predict(review)
     if prediction[0]==1:
          sentiment='Positive'
     else:
          sentiment='Negative'      
     return prediction[0],sentiment

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
     
     if request.method == 'POST':
        result = request.form
        content = request.form['review']
        review = pd.Series(content)
        prediction,sentiment =predictfunc(review)      
     return render_template("predict.html",pred=prediction,sent=sentiment)

if __name__ == '__main__':
     #app.run(debug = True,port=8080)
     app.run(host='0.0.0.0')