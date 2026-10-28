
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df_train = pd.read_csv("data/iris.csv")
feature_cols = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
X, y = df_train[feature_cols], df_train["Species"]
model = RandomForestClassifier(n_estimators=50, random_state=42).fit(X, y)
joblib.dump(model, "model.joblib")
print("Model trained and saved inside the container")
