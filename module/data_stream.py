import pandas as pd
from model.train_model import trainCategory


class DataStream:
    def __init__(self):
        dataset = pd.read_csv('./data/website_classification.csv')
        self.__df = dataset[['website_url',
                             'cleaned_website_text', 'Category']].copy()
        self.__X = self.__df['cleaned_website_text']
        self.__id_to_category = self.___create_category_id()

    def ___create_category_id(self):
        # Create a new column 'category_id' with encoded categories
        self.__df['category_id'] = self.__df['Category'].factorize()[0]
        category_id_df = self.__df[[
            'Category', 'category_id']].drop_duplicates()

        # Dictionaries for future use
        category_to_id = dict(category_id_df.values)
        return dict(
            category_id_df[['category_id', 'Category']].values)

    def getDF(self):
        return self.__df

    def getX(self):
        return self.__X

    def getCategoryId(self):
        return self.__id_to_category


def getCategoriesWiseCount(ds: DataStream) -> tuple[list, list]:
    """
    This method returns the Total Categories and their count
    """
    uniqueness = ds.getDF().groupby('Category').nunique()
    ud = uniqueness[['website_url']].copy()
    return list(ud.index), list(ud['website_url'])


def getTrainingData(yTrain) -> tuple[list, list]:
    """
    This method returns the Training data
    """
    yTrainCount = yTrain.value_counts()
    return list(yTrainCount.index), list(yTrainCount)


def getTestingData(yTesting) -> tuple[list, list]:
    """
    This method returns the Testing data
    """
    yTrainCount = yTesting.value_counts()
    return list(yTrainCount.index), list(yTrainCount)


def createOptions(title: str, labels: str, types: str, series: any):
    """
    Return the object
    """
    if isinstance(series[0], dict):
        dataSeries = []
        for data in series:
            dataSeries.append(data)
    elif types == 'bar':
        dataSeries = [{
            "data": series
        }]
    else:
        dataSeries = series

    return {
        "title": title,
        "labels": labels,
        "series": dataSeries,
        "type": types
    }


def getOptions(dataStream: DataStream):
    categories, categoriesWiseCount = getCategoriesWiseCount(dataStream)
    yTrain, yTest = trainCategory(dataStream.getX(), dataStream.getDF())
    testingCategories, testingCategoriesWiseCount = getTestingData(yTest)
    trainingCategories, trainingCategoriesWiseCount = getTrainingData(yTrain)
    data = {
        "categoriesWiseData": createOptions("Category Wise Count", categories, "bar", categoriesWiseCount),
        "testingAndTraining": createOptions("Category Wise Count (Training and Testing Data)", categories,
                                                    'bar', ({
                                                        "name": "Testing Data",
                                                        "data": testingCategoriesWiseCount
                                                    }, {
                                                        "name": "Training Data",
                                                        "data": trainingCategoriesWiseCount
                                                    },)),
        "trainingData": createOptions("Category Wise Count (Training Data)", trainingCategories, 'pie',
                                      trainingCategoriesWiseCount),
        "testingData": createOptions("Category Wise Count (Testing Data)", testingCategories, 'pie',
                                     testingCategoriesWiseCount)
    }
    return data
