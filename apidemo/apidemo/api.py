from ninja import NinjaAPI



app = NinjaAPI(title="Calculator API", version="1.0.0", description="A simple calculator API")



@app.get("/add", tags=["Add two numbers"])
def add(request, a: int, b: int):
    return {"result": a + b}

@app.get("/sub")
def sub(request, a: int, b: int):
    return {"result": a - b}

@app.get("/mul")
def mul(request, a: int, b: int):
    return {"result": a * b}

@app.get("/div")
def div(request, a: int, b: int):
    return {"result": a / b}

@app.get("/mod")
def mod(request, a: int, b: int):
    return {"result": a % b}

@app.get("/pow")
def pow(request, a: int, b: int):
    return {"result": a ** b}

@app.get("/sqrt")
def sqrt(request, a: int):
    return {"result": a ** 0.5}

@app.post("/add", tags=["Add two numbers"])
def add_post(request, a: int, b: int):
    return {"result": a + b}

@app.get("/hello", tags=["Hello World"])
def hello(request):
    return {"message": "Hello World!"}

@app.get("/greet", tags=["Hello World"])
def greet(request, name="Sourav"):
    return {"message": f"Hello {name}!"}