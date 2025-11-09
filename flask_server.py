def my_open(file_name):
    try:
        with open(file_name,"r") as fp:
            return fp.read()
    except Exception as e:
        return e


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "This is a api server for szzx"

@app.route('/<file>', methods=["GET"])
def get_json(file):
    try:
        if file in ("page0", "page1", "page2"):
            return my_open(f"{file}.json")
        else:
            raise Exception("404 Not Found")
    except Exception as e:
        raise
    

if __name__ == '__main__':
    app.run(port=80)
