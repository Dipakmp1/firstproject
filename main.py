from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)
data = pd.read_csv('Cleaned_data (2).csv')
pipe = pickle.load(open("RidgeModel (1).pkl", 'rb'))


@app.route('/')
def index():
    locations = sorted(data['Location'].unique())
    citi = sorted(data['City'].unique())
    return render_template('index.html', locations=locations, citi=citi)


@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    citi = request.form.get('citi')
    Bedrooms = request.form.get('No. of Bedrooms')
    Area = request.form.get('Area')
    pipe = pickle.load(open("RidgeModel (1).pkl", 'rb'))
    print(location, citi, Bedrooms, Area)
    input = pd.DataFrame([[location, citi, Area, Bedrooms]], columns=['Location', 'City', 'Area', 'No. of Bedrooms'])
    print(input)
    prediction = round(pipe.predict(input)[0])

    return str(prediction)

# demo():
#    location1 = data[data['City'] == 'Mumbai']
#    print(sorted(location1['Location'].unique()))

    return render_template(location1=location1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True, port=5001)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
