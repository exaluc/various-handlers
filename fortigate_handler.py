import requests

class FortinetHandler:
    def __init__(self, host, api_key):
        self.base_url = f"https://{host}/api/v2/"
        self.session = requests.Session()
        self.session.verify = False  # Disable SSL certificate validation. Consider enabling for production.
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}'
        })

    def get_address(self, address_name):
        endpoint = f"cmdb/firewall/address/{address_name}"
        response = self.session.get(self.base_url + endpoint)
        return response.json()

    def create_address(self, address_name, ip):
        endpoint = "cmdb/firewall/address/"
        data = {
            "name": address_name,
            "type": "ipmask",
            "subnet": f"{ip} 255.255.255.255"
        }
        response = self.session.post(self.base_url + endpoint, json=data)
        return response.json()

    def delete_address(self, address_name):
        endpoint = f"cmdb/firewall/address/{address_name}"
        response = self.session.delete(self.base_url + endpoint)
        return response.json()

# Example usage:

fortinet = FortinetHandler(host="YOUR_FORTINET_HOST", api_key="YOUR_API_KEY")

# Create an address
print(fortinet.create_address("Test_Address", "192.168.1.100"))

# Get an address's details
print(fortinet.get_address("Test_Address"))

# Delete an address
print(fortinet.delete_address("Test_Address"))
