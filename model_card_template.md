# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model predicts wheter a person will earn more or less than $50k USD, by using features like gender, number of work hours per week, maximum level of education and more.

## Intended Use
This model could be use to estimate the potential salary of a new hire.

## Training Data
Training data is 80% of the total, and it comes from https://archive.ics.uci.edu/ml/datasets/census+income

## Evaluation Data
Evaluation data is 20% of the total, and it comes from https://archive.ics.uci.edu/ml/datasets/census+income

## Metrics
The model was evaluated by using precision, recall, fbeta. THe best experiment gave the following metrics precision=0.64. recall=0.59, fbeta=0.61

## Ethical Considerations
The model uses personal information to make the predictions and features like gener and race. Model bias could be an issue.

## Caveats and Recommendations
We could consider the following
    - Add city where they live as a featyres, bigger cities tend to pay more.
    - Add specific profession, working in tech, pays more.
    - 