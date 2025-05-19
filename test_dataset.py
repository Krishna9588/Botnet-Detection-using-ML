import pandas as pd

# Load original combined dataset
df_attack = pd.read_csv("dataset/CTU13_Attack_Traffic.csv")
df_normal = pd.read_csv("dataset/CTU13_Normal_Traffic.csv")

df_attack["Label"] = 1
df_normal["Label"] = 0

df_combined = pd.concat([df_attack, df_normal], ignore_index=True)
df_combined = df_combined.sample(n=10)  # take 10 random rows

# Drop the Label column to simulate "unknown" traffic
df_combined.drop(columns=["Label"], inplace=True)

# Save to test_sample.csv
df_combined.to_csv("dataset/test_sample.csv", index=False)

print("✅ test_sample.csv generated at dataset/test_sample.csv")
