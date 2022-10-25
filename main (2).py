import pandas as pd

from model.train_model import train_the_model
from module.data_module import DataStream
from module.scrap_tool import ScrapTool
from module.clean_text import clean_text
from module.visualization import createHBar, createPieChart

website = input("Enter enter any website url: ")
print("Please wait website is analysing...")

ds = DataStream()
fitted_vectorizer, m1 = train_the_model(ds.getX(), ds.getDF())
scrapTool = ScrapTool()
try:
    web = dict(scrapTool.visit_url(website))
    text = (clean_text(web['website_text']))
    t = fitted_vectorizer.transform([text])
    print(ds.getCategoryId()[m1.predict(t)[0]])
    if input("Do you want to view the graph (Yes/No): ").lower() in ("yes", "y"):
        data = pd.DataFrame(m1.predict_proba(
            t)*100, columns=ds.getDF()['Category'].unique())
        data = data.T
        data.columns = ['Probability']
        data.index.name = 'Category'
        a = data.sort_values(['Probability'], ascending=False)
        a['Probability'] = a['Probability'].apply(
            lambda x: round(x, 2))
        a = a[a['Probability'] >= 1]
        createPieChart(a['Probability'], a.index)
except Exception as e:
    print(e)
    print("Connection Timedout!")
