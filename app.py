from flask import Flask
from crypt import methods

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return "Starting machine learning project"

if __name__=='__main__':
    app.run(debug=True)    