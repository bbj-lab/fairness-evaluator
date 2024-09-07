from setuptools import find_packages, setup

setup(
  name="mlflow-fairness-plugin",
  version="0.0.1",
  description="Fairness evaluation plugin for MLflow",
  packages=find_packages(),
  # Require MLflow as a dependency of the plugin, so that plugin users can simply install
  # the plugin & then immediately use it with MLflow
  install_requires=["mlflow"],
  entry_points={
    # Define a MLflow model evaluator with name "dummy_evaluator"
    "mlflow.model_evaluator": (
        "fairness_evaluator=mlflow_fairness_plugin.fairness_evaluator:FairnessEvaluator"
    )     
  }
)