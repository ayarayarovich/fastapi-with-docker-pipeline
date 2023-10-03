from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    with open('resources/jopa.txt', 'r') as file:
        data = file.read()
    return {"data": data, "pidor": "huetahunesa"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
