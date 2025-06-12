import joblib
import pandas as pd

def model_fn(model_dir):
    model = joblib.load(f"{model_dir}/model.joblib")
    return model

def input_fn(request_body, request_content_type):
    if request_content_type == "csv":
        return pd.read_csv(request_body)
    raise ValueError("Unsupported content type :{}".format(request_content_type))

def predict_fn(input_data, model):
    return model.predict(input_data)

def output_fn(prediction, content_type):
    return ",".join(str(x) for x in prediction)