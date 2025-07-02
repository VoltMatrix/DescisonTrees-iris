# DescisonTrees-iris

# Decision Tree on Iris Dataset

This repository contains Python code demonstrating the use of a Decision Tree Classifier and Regressor on the Iris dataset using Scikit-learn. It includes training a decision tree, visualizing it using Graphviz, and making predictions.

## Overview
The code performs the following tasks:
- Loads the Iris dataset and uses petal length and width as features.
- Trains a `DecisionTreeClassifier` with a maximum depth of 2.
- Visualizes the decision tree by generating a `.dot` file and converting it to a PNG image using Graphviz.
- Makes a sample prediction for a new input.
- Demonstrates a `DecisionTreeRegressor` (though the Iris dataset is typically used for classification).

## Requirements
- Python 3.x
- Scikit-learn
- Graphviz (for visualization)
- Optional: `subprocess` (included in standard Python library)

Install Python dependencies:
```bash
pip install scikit-learn
