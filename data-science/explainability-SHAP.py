import shap
import xgboost as xgb

# Train a model
model = xgb.XGBClassifier()
model.fit(X_train, y_train)

# SHAP explainability
explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

# Visualization
shap.summary_plot(shap_values, X_test)
