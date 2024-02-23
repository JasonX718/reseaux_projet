from flask import Flask, request

app = Flask(__name__)

@app.route('/update', methods=['GET'])
def update():
    temperature = request.args.get('temperature')
    humidity = request.args.get('humidity')
    # Process and/or store the data here
    print(f"Received temperature: {temperature}, humidity: {humidity}")
    return "Data Received"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
