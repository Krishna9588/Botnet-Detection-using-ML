import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
import joblib
import os

attack_file = "dataset/CTU13_Attack_Traffic.csv"
normal_file = "dataset/CTU13_Normal_Traffic.csv"

df_attack = pd.read_csv(attack_file)
df_normal = pd.read_csv(normal_file)

# Label the datasets
df_attack["Label"] = 1  # Botnet
df_normal["Label"] = 0  # Normal

# Combine both the files
df = pd.concat([df_attack, df_normal], ignore_index=True)
df = shuffle(df).reset_index(drop=True)

# Drop non-numeric columns (except protocol)
drop_cols = ["StartTime", "SrcAddr", "DstAddr", "State", "sTos", "dTos", "Dir", "SrcMac", "DstMac", "SrcPt", "DstPt", "TotFwdPkts", "TotBwdPkts"]
df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors='ignore')

# Encode protocol if exists
if 'Proto' in df.columns:
    le = LabelEncoder()
    df['Proto'] = le.fit_transform(df['Proto'])

# Drop rows with NaN or infinite
df = df.replace([float('inf'), -float('inf')], pd.NA)
df = df.dropna()

# Features and target
X = df.drop("Label", axis=1)
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/botnet_rf_model.joblib")
print("✅ Model saved to models/botnet_rf_model.joblib")