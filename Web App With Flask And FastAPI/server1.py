from flask import Flask 
from scrape import render
from logger import trigger_log_save

# from gunicorn import gunicorn

app = Flask(__name__)

# http://localhost:5000/
@app.route("/", methods=['GET'])
def hello_world():
    return "Hello World"


# http://localhost:5000/scrape
@app.route("/scrape", methods=['GET'])
def web_scrape():
    trigger_log_save()
    render()
    #render(start_year=2010, years_ago=1)
    return {"data" : "Web scraping done"}


if __name__ == "__main__":
    app.run(port=8000) #default is 5000