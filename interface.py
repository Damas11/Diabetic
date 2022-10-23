from flask import Flask,jsonify,render_template,request,json
from utilis import Diabetic
import config


app=Flask(__name__)
@app.route('/')
def hello_flask():
    print('Welcome to flask')


@app.route('/predict_diabetics')
def get_predict():
    data=request.form
    print('Data is ',data)
    Glucose=eval(data['Glucose'])
    BloodPressure=eval(data['BloodPressure'])
    SkinThickness=eval(data['SkinThickness'])
    Insulin=eval(data['Insulin'])
    BMI=eval(data['BMI'])
    DiabetesPedigreeFunction=eval(data['DiabetesPedigreeFunction'])
    Age=eval(data['Age'])

    diab_ins=Diabetic(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    charges=diab_ins.get_predicted_charges()
    if charges==0:
        print("Person is not Diabetic")

    else:
        print('Person is Diabetic')

    return (f"the person has  {charges}")


if __name__=='__main__':
    app.run(host='0.0.0.0',port=config.PORT_NUMBER,debug=False)

