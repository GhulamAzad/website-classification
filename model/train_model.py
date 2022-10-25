from pandas import DataFrame
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV


class MLModel:
    def __init__(self, X, df: DataFrame):
        self.__X_train, self.__X_test, self.__y_train, self.__y_test = train_test_split(X, df['category_id'],
                                                                                        test_size=0.25,
                                                                                        random_state=0)

        self.__tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5,
                                       ngram_range=(1, 2),
                                       stop_words='english')

        self.__fittedVectorized = self.__tfidf.fit(self.__X_train)
        self.__tfidfVectorizedVectors = self.__fittedVectorized.transform(self.__X_train)

        self.__m = LinearSVC().fit(self.__tfidfVectorizedVectors, self.__y_train)
        self.__probabilityModel = CalibratedClassifierCV(base_estimator=self.__m,
                                                         cv="prefit").fit(self.__tfidfVectorizedVectors, self.__y_train)

    def getXTrain(self):
        return self.__X_train

    def getXTest(self):
        return self.__X_test

    def getYTrain(self):
        return self.__y_train

    def getYTest(self):
        return self.__y_test

    def getFittedVectorized(self):
        return self.__fittedVectorized

    def getProbabilityModel(self):
        return self.__probabilityModel


def trainCategory(X, df: DataFrame):
    y = df['Category']  # Target or the labels we want to predict

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.25,
                                                        random_state=0)
    return y_train, y_test
