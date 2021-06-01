from geopy.geocoders import Nominatim
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def maps_api():
    lat = request.args.get('lat')
    long = request.args.get('long')
    cords = lat + ', '+long
    geolocator = Nominatim(user_agent="http")
    location = geolocator.reverse(cords)
    return location.address
