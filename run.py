#!flask/bin/python
from app import app
app.run(host="0.0.0.0", port=int("8080"), debug=True)
