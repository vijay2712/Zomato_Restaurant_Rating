import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')

def home():
    return render_template('Zomato.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
        For rendering results on HTML GUI
    '''
    features=[int(x) for x in request.form.values()]
    final_features=[np.array(features)]
    prediction =model.predict(final_features)

    output=round(prediction[0],1)

    return render_template('Zomato.html',prediction_text='your rating is:{}'.format(output))

if __name__=="__main__":
    app.run(debug=True)





