from module.scrap_tool import ScrapTool
from module.clean_text import clean_text
from model.train_model import MLModel
from module.data_stream import DataStream, createOptions
import pandas as pd


def predictCategory(website: str, mlModel: MLModel, ds: DataStream):
    """
    Scrap the data from the website and predict the category and return the probability category list
    """
    scrapTool = ScrapTool()
    web = dict(scrapTool.visit_url(website))
    text = (clean_text(web['website_text']))
    t = mlModel.getFittedVectorized().transform([text])

    predictedCategory = ds.getCategoryId(
    )[mlModel.getProbabilityModel().predict(t)[0]]

    data = pd.DataFrame(mlModel.getProbabilityModel().predict_proba(
        t) * 100, columns=ds.getDF()['Category'].unique())
    data = data.T
    data.columns = ['Probability']
    data.index.name = 'Category'
    a = data.sort_values(['Probability'], ascending=False)
    a['Probability'] = a['Probability'].apply(
        lambda x: round(x, 2))
    # a = a[a['Probability'] >= 1]

    data = {
        "predictedCategory": predictedCategory,
        "chartOption": {
            "resultData": createOptions(f"Probability Prediction for each Category of the {website}", list(a.index), 'pie', list(a['Probability']))
        }
    }

    return data
