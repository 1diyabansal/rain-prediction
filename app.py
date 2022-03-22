from pred import print_probs, evidence
from flask import Flask, request, jsonify, render_template
#from model import evidence, print_probs
app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def Home():
    return render_template('index.html')
@app.route('/predict',methods=['POST','GET'])
def predict():

    if request.method == 'POST':
        time = str(request.form['Time'])
        humidity = int(request.form['Humidity'])
        wind_gust = int(request.form['Wind_gust'])

        time = 'H' + time

        if humidity <= 60:
            humidity = '<=60'
        else:
            humidity = '>60'

        if wind_gust <= 40:
            wind_gust = '<=40'
        elif wind_gust > 40 and wind_gust < 50:
            wind_gust = '40-50'
        else:
            wind_gust = '>50'
        evidence('ev1', time, humidity, 1.0)
        evidence('ev2', 'W', wind_gust, 1.0)
        rt_chances = print_probs()
        return render_template('index.html',prediction_text="There chances of tomorrow Rain is {}".format(rt_chances))
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
