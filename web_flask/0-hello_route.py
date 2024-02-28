#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask

app = Flask("my_custom_name")

@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
        """
            Returns a message when accessing the route /airbnb-onepage/
                """
                    return "Hello HBNB!"

                if __name__ == "__main__":
                        app.run(host='100.25.194.180', port=5000)
