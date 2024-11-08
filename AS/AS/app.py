
from flask import Flask, request

app = Flask(__name__)

# Store DNS records in memory
dns_records = {
    "fibonacci.com": "127.0.0.1"
}

@app.route('/register', methods=['PUT'])
def register():
    hostname = request.args.get('hostname')
    ip_address = request.args.get('ip')
    if not hostname or not ip_address:
        return "Missing parameters", 400

    dns_records[hostname] = ip_address
    return f"Hostname {hostname} registered with IP {ip_address}", 200

@app.route('/resolve', methods=['GET'])
def resolve():
    hostname = request.args.get('hostname')
    if not hostname:
        return "Missing hostname", 400

    ip_address = dns_records.get(hostname)
    if not ip_address:
        return "Hostname not found", 404

    return ip_address, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=53533)

