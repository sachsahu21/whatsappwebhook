from flask import Flask, request
app = Flask(__name__)

@app.route("/w",methods=["POST"])
def hook():
  print(request.data)
  return "hello world"

if __name__=="__main__":
   app.run(port=5001)
# url = "http://127.0.0.1:5001/w"

# r = requests.post(url)
# print(r.content)