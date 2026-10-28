
import pandas as pd
import pytest
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

@pytest.fixture(scope="module")
def data():
    return pd.read_csv("data/iris.csv")

# ---------- DATA TESTS ----------
def test_no_missing_values(data):
    assert data.isnull().sum().sum() == 0

def test_expected_columns(data):
    assert "Species" in data.columns
    expected_cols = {"SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"}
    assert expected_cols.issubset(set(data.columns))

def test_feature_ranges(data):
    assert (data["SepalLengthCm"] > 0).all()
    assert (data["SepalWidthCm"] > 0).all()
    assert (data["PetalLengthCm"] > 0).all()
    assert (data["PetalWidthCm"] > 0).all()
    assert data["Species"].isin(["setosa", "versicolor", "virginica"]).all()

# ---------- MODEL TESTS ----------
def test_model_accuracy_above_threshold(data):
    feature_cols = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
    X, y = data[feature_cols], data["Species"]
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    model = RandomForestClassifier(n_estimators=50, random_state=42).fit(Xtr, ytr)
    assert accuracy_score(yte, model.predict(Xte)) >= 0.85

def test_model_prediction_shape(data):
    feature_cols = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
    X, y = data[feature_cols], data["Species"]
    model = RandomForestClassifier(n_estimators=10, random_state=0).fit(X, y)
    assert len(model.predict(X.iloc[:7])) == 7
