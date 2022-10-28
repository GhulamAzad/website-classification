from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


from module.data_stream import DataStream, getOptions
from model.train_model import MLModel, trainCategory
from module.predict import predictCategory

app = FastAPI()
app.add_middleware(HTTPSRedirectMiddleware)


dataStream = DataStream()
mlModel = MLModel(dataStream.getX(), dataStream.getDF())

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def getTotalCountDataset():
    yTrain, yTest = trainCategory(dataStream.getX(), dataStream.getDF())
    data = {
        "totalData": len(dataStream.getDF().index),
        "totalTrainingData": len(yTrain.index),
        "totalTestingData": len(yTest.index)
    }
    return data


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": getTotalCountDataset()})


@app.post("/predict")
async def predict(request: Request):
    form = await request.form()
    try:
        data = predictCategory(form.get('website_url'), mlModel, dataStream)
        data["isPredictedData"] = True
        data.update(getTotalCountDataset())
        return templates.TemplateResponse("index.html", {"request": request, "data": data})
    except Exception as e:
        print(e)
    return templates.TemplateResponse("index.html", {"request": request, "data": getTotalCountDataset()})


@app.get("/prediction", response_class=HTMLResponse)
async def prediction(request: Request):
    data = getOptions(dataStream)
    return templates.TemplateResponse("prediction.html", {"request": request, "data": data})


@app.get("/team", response_class=HTMLResponse)
async def prediction(request: Request):
    return templates.TemplateResponse("team.html", {"request": request})
