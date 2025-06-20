from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route('/')
def index():
    return "Welcome to the prediction model. Use /predict command to make predictions. "


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    print("Полученные данные:", data)

    if "option" in data.keys():
        option = data["option"]
        if option == 1:
            test_data = [[2.0, 3.0, 1.0, 0.0, 0.0, 18.0, 2.0, 9.0, 3.5, 4.0, 5.0, 8.0, 0.0, 10.0, 5.0, 12.0, 6.2, 210.75]]
            prediction = model.predict(test_data)

        elif option == 2:
            test_data = [[1.0, 4.0, 0.0, 0.0, 1.0, 21.0, 1.0, 11.0, 4.0, 5.0, 4.0, 10.0, 1.0, 13.0, 6.0, 15.0, 4.543491, 228.33]]
            prediction = model.predict(test_data)

        elif option == 3:
            test_data = [[2.0, 1.0, 1.0, 3.0, 2.0, 0.0, 1.0, 11.0, 2.0, 3.0, 3.0, 2.0, 1.0, 13.0, 2.0, 2.0, 2.0, 134.41]]
            prediction = model.predict(test_data)

        else:
            test_data = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.99, 0.0]]
            prediction = model.predict(test_data)
    else:
        test_data = {"PreferredLoginDevice": 2.0, "PreferredPaymentMode": 1.0, "Gender": 1.0, "PreferedOrderCat": 3.0,
            "MaritalStatus": 2.0, "Tenure": 0.0, "CityTier": 1.0, "WarehouseToHome": 11.0, "HourSpendOnApp": 2.0,
            "NumberOfDeviceRegistered": 3.0, "SatisfactionScore": 3.0, "NumberOfAddress": 2.0, "Complain": 1.0,
            "OrderAmountHikeFromlastYear": 13.0, "CouponUsed": 2.0, "OrderCount": 2.0, "DaySinceLastOrder": 2.0,
            "CashbackAmount": 134.41}
        for i in data.keys():
            if i in test_data.keys():
                test_data[i] = data[i]

        prediction = model.predict(test_data)

    return prediction


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
