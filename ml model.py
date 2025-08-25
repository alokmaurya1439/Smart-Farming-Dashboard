import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# -------------------------------
# Step 1: Load Dataset Safely
# -------------------------------
local_path = "Crop_recommendation.csv"
kagglehub_path = r"D:/Smart Farming Dashboard/Crop_recommendation.csv"

if os.path.exists(local_path):
    data = pd.read_csv(local_path)
elif os.path.exists(kagglehub_path):
    data = pd.read_csv(kagglehub_path)
else:
    raise FileNotFoundError("❌ Crop_recommendation.csv not found. Please place it in project folder or update path.")

print("✅ Dataset loaded successfully!")
print(data.head())

# -------------------------------
# Step 2: Prepare Data
# -------------------------------
X = data.drop("label", axis=1)
y = data["label"]

# -------------------------------
# Step 3: Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# Step 4: Train Model
# -------------------------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -------------------------------
# Step 5: Evaluate
# -------------------------------
preds = model.predict(X_test)
print("✅ Model Training Complete!")
print("🎯 Accuracy:", accuracy_score(y_test, preds))

# -------------------------------
# Step 6: Save Model
# -------------------------------
joblib.dump(model, "crop_model.pkl")
print("💾 Model saved as crop_model.pkl")

