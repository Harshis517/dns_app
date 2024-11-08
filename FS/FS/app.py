
from flask import Flask, request

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    # Retrieve query parameters
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    # Validate that none of the parameters are missing
    if not all([hostname, fs_port, number, as_ip, as_port]):
        return 'Bad Request: Missing parameters', 400

    # Validate that 'number' is an integer
    if not number.isdigit():
        return 'Bad Request: Number must be an integer', 400

    return f"Hostname: {hostname}, fs_port: {fs_port}, number: {number}, as_ip: {as_ip}, as_port: {as_port}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

