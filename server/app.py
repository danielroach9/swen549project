"""
    The Flask app
    In a separate file to avoid circular imports

    Date - 11/2/17
    Author - Philip Bedward, Daniel Roach, Sadaf Chowdhury, Daniel Darius Cox
"""
from flask import Flask
APP = Flask(__name__,static_folder="../client/dist",template_folder="../client")

