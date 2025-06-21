from app import app


def test_home():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200


def test_predict():
    client = app.test_client()
    payload = {"option": 1}

    response = client.post("/predict", json=payload)
    if response.status_code == 200:
        raise f"Can not get the access to website: {response.status_code}"

    try:
        text = response.get_data(as_text=True)
    except Exception as e:
        raise e

    if type(text) != str:
        raise f"Wrong return type: {type(text)}"

    if int(text) != 1:
        raise f"Wrong answer: {text}.\n Expected: 1.0"


if __name__ == "__main__":
    test_home()
    test_predict()