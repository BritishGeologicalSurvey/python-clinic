"""Demo Flask app to render borehole tables via API"""
import json

from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)


@app.route("/borehole/<number>")
def borehole(number=None):
    """Get borehole data from API and populate template table"""
    borehole_data = get_borehole_data(number)
    return render_template('borehole.html', number=number,
                           borehole_data=borehole_data)


def get_borehole_data(number):
    """Query HTTP endpoint for borehole data"""
    # Get data
    url = f"http://localhost:8000/borehole/{number}"
    response = requests.get(url)
    # Load twice to clear character escaping
    return json.loads(json.loads(response.text))
