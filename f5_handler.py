import requests
import json

class F5Handler:
    def __init__(self, host, username, password):
        self.base_url = f"https://{host}/mgmt/tm/"
        self.session = requests.Session()
        self.session.verify = False  # Disable SSL certificate validation. Consider enabling for production.
        self.session.headers.update({
            'Content-Type': 'application/json'
        })
        self.session.auth = (username, password)

    def get_pool(self, pool_name):
        endpoint = f"ltm/pool/~Common~{pool_name}"
        response = self.session.get(self.base_url + endpoint)
        return response.json()

    def create_pool(self, pool_name):
        endpoint = "ltm/pool"
        data = {
            "name": pool_name,
            "partition": "Common"
        }
        response = self.session.post(self.base_url + endpoint, data=json.dumps(data))
        return response.json()

    def delete_pool(self, pool_name):
        endpoint = f"ltm/pool/~Common~{pool_name}"
        response = self.session.delete(self.base_url + endpoint)
        return response.json()

# Example usage:

f5 = F5Handler(host="YOUR_F5_HOST", username="YOUR_USERNAME", password="YOUR_PASSWORD")

# Create a pool
print(f5.create_pool("test_pool"))

# Get a pool's details
print(f5.get_pool("test_pool"))

# Delete a pool
print(f5.delete_pool("test_pool"))
