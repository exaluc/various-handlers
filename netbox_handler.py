import pynetbox

class NetBoxHandler:
    def __init__(self, url, token):
        self.nb = pynetbox.api(url, token=token)

    def get_sites(self):
        """Retrieve all sites"""
        return self.nb.dcim.sites.all()

    def get_devices(self):
        """Retrieve all devices"""
        return self.nb.dcim.devices.all()

    def create_site(self, data):
        """Create a new site"""
        return self.nb.dcim.sites.create(data)

    def create_device(self, data):
        """Create a new device"""
        return self.nb.dcim.devices.create(data)

# Initialize the NetBoxHandler
nb_handler = NetBoxHandler('http://your-netbox-url', 'your-api-token')

# Get all sites
sites = nb_handler.get_sites()
for site in sites:
    print(site)

# Get all devices
devices = nb_handler.get_devices()
for device in devices:
    print(device)

# Create a new site
new_site_data = {
    'name': 'New Site',
    'slug': 'new-site',
}
new_site = nb_handler.create_site(new_site_data)
print(f"New site created: {new_site}")

# Create a new device
new_device_data = {
    'name': 'New Device',
    'device_type': 'some-device-type',
    'device_role': 'some-device-role',
    'site': 'site-id',  # Replace with actual site id
}
new_device = nb_handler.create_device(new_device_data)
print(f"New device created: {new_device}")
