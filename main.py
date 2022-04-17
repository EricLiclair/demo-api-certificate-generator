from fastapi import FastAPI
import time
app = FastAPI()


@app.get("/")
async def root():
  time.sleep(2)
  return {
    "certificate_url": "https://storage.googleapis.com/generator-certificate.appspot.com/public/ASJ_2021/ASJ_2021_23761672.png",
    "date": "Fri, 08 Apr 2022 00:00:00 GMT",
    "id": "ASJ_2021_23761672",
    "name": "Aman Kumar",
    "event_name": "ASJ_2021"
}