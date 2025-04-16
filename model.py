import joblib

MODEL_PATH = "engagement_model.joblib"

def load_model():
    return joblib.load(MODEL_PATH)

def predict_engagement(model, input_df):
    input_df = input_df.fillna(0)
    return model.predict(input_df)[0]
