from fastapi import FastAPI

app = FastAPI()


@app.get("/add")
async def root(x: int = 0, y: int = 0):
    return {
            'valor de x: ': x,
            'valor de y: ': y,
            'soma': x + y,
            }

@app.get("/sub")
async def root(x: int = 0 , y: int = 0):
    return {
            'valor de x: ': x,
            'valor de y: ': y,
            'subtraçao': x - y,
            }

@app.get("/mult")
async def root(x: int = 0 , y: int = 0):
    return {
            'valor de x: ': x,
            'valor de y: ': y,
            'multiplicaçao': x * y,
            }

@app.get("/div")
async def root(x: int = 0 , y: int = 0):
    return {
            'valor de x: ': x,
            'valor de y: ': y,
            'divisao': x / y,
            }
