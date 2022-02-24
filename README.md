# ML model API on Heroku

This is the third Udacity project of the MLOps Nanodegree, where I published an API on Heroku, which estimates whether an user will earn more or less than $50k USD.

## Model
This is a classification problem where we used a user background to determine if they will earn more or less than $50k USD/year. Please read the [Model Card](model_card_template.md) for a more detailed description.

## Components
Below you can see the steps that you could follow in order to run the app locally.

- Clean dataset `python starter/ml/data_cleaning.py`
- Training: `python starter/train_model.py`
- Run app: `uvicorn main:app --reload`
- Test the app: `pytest test_local.py`
- Test a request: `python sample_request.py` 

## CI/CD
The CI step is implemented using GitHub actions, then automatic deploys are activated on Heroku (CD).

## Results
- [continuous_deployment](screenshots/continuous_deployment.png)
- [continuous_integration](screenshots/continuous_integration.png)
- [dvc_dag](screenshots/dvc_dag.png)
- [example](screenshots/example.png)
- [live_get](screenshots/live_get.png)
- [live_post](screenshots/live_post.png)
