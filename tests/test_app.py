import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import flask_app


tester = flask_app.test_client()


def test_home():
    response = tester.get("/")
    assert response.status_code == 200


def test_predict():
    print("Testing different options (from 1 to 4)")
    for i in range(1, 5):
        payload = {"option": i}

        response = tester.post("/predict", json=payload)
        if response.status_code == "200":
            raise Exception(f"Can not get the access to website: {response.status_code}")

        try:
            text = response.get_data(as_text=True)
        except Exception as e:
            raise e

        try:
            text = float(text)
        except Exception as e:
            raise e

        if float(text) != 1:
            raise Exception(f"Wrong answer: {text}.\n Expected: 1.0")


if __name__ == "__main__":
    test_home()
    test_predict()
