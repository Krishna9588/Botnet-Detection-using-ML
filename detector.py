import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load model
model = joblib.load("models/botnet_rf_model.joblib")

# Load test data
df = pd.read_csv("dataset/test_sample.csv")

# Backup the original for output
df_original = df.copy()

# Drop columns not used during training
drop_cols = ["StartTime", "SrcAddr", "DstAddr", "State", "sTos", "dTos", "Dir", "SrcMac", "DstMac", "SrcPt", "DstPt", "TotFwdPkts", "TotBwdPkts", "Label"]
df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors='ignore')

# Encode Proto if needed
if 'Proto' in df.columns:
    le = LabelEncoder()
    df['Proto'] = le.fit_transform(df['Proto'])

# Handle missing/infinite values
df = df.replace([float('inf'), -float('inf')], pd.NA)
df = df.dropna()

# Predict
predictions = model.predict(df)

# Append predictions to the original
df_original["Prediction"] = predictions
df_original["Prediction_Label"] = df_original["Prediction"].apply(lambda x: "BOTNET" if x == 1 else "NORMAL")

# Output results
print(df_original[["Prediction_Label"]])

output = "dataset/prediction_output.csv"
# Optionally save results
df_original.to_csv(output, index=False)
print(f"Predictions saved to {output}")
