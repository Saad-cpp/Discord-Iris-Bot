from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd


df = pd.read_csv(r"E:\Downloads\Compressed\archive_3\iris.csv")
x = df.drop(["species"], axis=1)
y = df["species"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
nb = GaussianNB()
nb.fit(x_train, y_train)


def get_accuracy():
    return accuracy_score(y_test, nb.predict(x_test))


def predict_result(x_pred):
    x_pred = pd.DataFrame(
        [x_pred], columns=["sepal_length", "sepal_width", "petal_length", "petal_width"]
    )
    return nb.predict(x_pred)
