from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('mcm_executed.csv', index_col=0)

@app.route('/get_csv_data', methods=['GET'])
def get_csv_data():
    return jsonify(df.to_dict())

if __name__ == '__main__':
    app.run(port=5000)
