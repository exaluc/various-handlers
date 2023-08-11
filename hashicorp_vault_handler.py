import hvac

class VaultHandler:
    def __init__(self, url, token):
        self.client = hvac.Client(url=url, token=token)

    def read_secret(self, path):
        return self.client.secrets.kv.v2.read_secret_version(path=path)

    def write_secret(self, path, secret):
        self.client.secrets.kv.v2.create_or_update_secret(path=path, secret=secret)

    def delete_secret(self, path):
        self.client.secrets.kv.v2.delete_secret_versions(path=path)

vault = VaultHandler('http://localhost:8200', 'your-token-here')

# Write a secret
vault.write_secret('my-secret', {'username': 'user', 'password': 'pass'})

# Read a secret
print(vault.read_secret('my-secret'))

# Delete a secret
vault.delete_secret('my-secret')
