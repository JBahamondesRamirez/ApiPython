from fastapi import *
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from model.crud import DAO
from model.schemas import *

Dao = DAO()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get("/getStops")
def getStops():
    return Dao.getStops()

@app.post("/calculateCoste")
def calculateCoste(coste:Coste):
    return Dao.calculateCoste(coste)

@app.post("/insertStop")
def insertStop(parade:Stop):
    return Dao.insertStop(parade)
