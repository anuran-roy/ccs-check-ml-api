# Descriptive Answer-checking API for IEEE CS CCS 2022

## Deployed on:

### [**Heroku Deployment**](https://ccs-checking-api.herokuapp.com/)

## Endpoints:

1. ### **```/check/descriptive/```:**
   
   **Request type:** POST

   **Summary**:
        Checks for relevance of descriptive answer.


    **Request type**: POST


    **Request body type**:

    1. **answer**: string containing answer given by participant \
    2. **keywords**: Optional list of strings containing keywords for the answer \
    3. **model_answer**: Optional string containing model answer


    **Returns**: Dictionary/Object containing relevance score

    **Example:**

    1. Request Body:
    <br><br>

    ```json
    {
        "given_answer": "Hello",
        "keywords": ["hello"],
        "model_answer": "Hello there!"
    }
    ```

    Response Body:
    <br><br>
    ```json
    {
        "status": 200,
        "score": 1.0
    }
    ```

    ## Usage:

    1. ### Python:

    ```python
    import requests

    response = requests.post(
        "https://ccs-checking-api.herokuapp.com/check/descriptive/",
        json={
            "given_answer": "Hello",
            "keywords": ["hello"],
            "model_answer": "Hello there!",
        },
    )

    print(response.json())
    ```