from flask import Flask,request,jsonify
import util

app= Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response=jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price',methods=['POST'] ) # http GET and POST
def predict_home_price():
    location=request.form['location']
    total_sqft=float(request.form['total_sqft'])
    bath=int(request.form['bath'])
    bhk=int(request.form['bhk'])

    response=jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bath,bhk)
    })

    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__=="__main__":
    print("Starting Python Flask server for Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(host='0.0.0.0', port=5000)