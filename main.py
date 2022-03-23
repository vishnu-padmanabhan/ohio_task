from flask import Flask, render_template, request, jsonify
import logical_layer.data_processing as dp

app = Flask(__name__)


@app.route('/')
def index():
    dp.load_db()
    return render_template('index.html')


@app.route('/data', methods=['GET'])
def get_data():
    well_number = request.args.get('well')
    data = dp.get_data(well_number)
    if data:
        return jsonify(data), 200
    return jsonify({'message': 'No data found'}), 404


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
