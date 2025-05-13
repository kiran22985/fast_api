from fastapi import FastAPI

app= FastAPI()


@app.get("/")
def read_post():
    return {"message":"Hello Kiran user"}


    


