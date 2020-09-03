from fastapi import FastAPI
import uvicorn
from scrape import render
from logger import trigger_log_save

app = FastAPI()

# http://localhost:5000/
@app.get("/")
def hello_world():
    return {"data":[1,2,3,4]}

# http://localhost:5000/scrape
@app.get("/scrape")
def scrape():
    trigger_log_save() # for logging the timestamp when scraper was triggered
    render(start_year=2015, years_ago=3)
    return {"data": "Web scraping done"}


if __name__ == "__main__":
    uvicorn.run("server2:app", host="127.0.0.1", port=5000)

