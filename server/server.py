from flask import Flask, request, jsonify
import util
app = Flask(__name__)


# Get location names
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# The user post their input and the server will return the estimated price
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    
    # location,distance,bedroom2,bathroom,car,landsize,buildingArea,yearBuilt,lattitude,longtitude,htype,ttype
    
    location = request.form['location']
    house_type = int(request.form['house_type'])
    distance = float(request.form['distance'])
    bedroom = int(request.form['bedroom'])
    bathroom = int(request.form['bathroom'])
    car = int(request.form['car'])
    landsize = float(request.form['landsize'])
    buildingarea = float(request.form['buildingarea'])
    yearbuilt = float(request.form['yearbuilt'])
    lattitude = float(request.form['lattitude'])
    longtitude = float(request.form['longtitude'])
    
    response = jsonify({
        'estimated_price': util.get_estimated_price(location,house_type,distance,bedroom,bathroom,car,landsize,buildingarea,yearbuilt,lattitude,longtitude)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)



