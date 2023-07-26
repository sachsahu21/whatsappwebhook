from flask import Flask
app = Flask(__name__)

# print (__name__)

@app.route("/hi",methods=['GET'])
def home():
  return "Hello, Sachin!"

@app.route("/hi2",methods=['GET'])
def home2():
   return "Hello, Valerie!"



if __name__ == '__main__':
  app.run(port=5001,debug=True)