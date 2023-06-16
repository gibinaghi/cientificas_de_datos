from flask import Flask

def test_unit():
    app = Flask(__name__)
    assert app is not None, "Error: Flask app is not initialized"
    print ("listo")

# Prueba de la función test_unit
test_unit()
