import mlflow

eval_data = ...  # Define eval_data here

with mlflow.start_run() as run:
    results = mlflow.evaluate(
        model="endpoints:/databricks-mpt-7b-instruct",
        data=eval_data,
        inference_params={"max_tokens": 100, "temperature": 0.0},
        model_type="text",
    )