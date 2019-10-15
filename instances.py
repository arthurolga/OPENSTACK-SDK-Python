import openstack

# Initialize and turn on debug logging
openstack.enable_logging(debug=True)

# Init cloud
conn = openstack.connection.Connection(
    auth_url='http://192.168.0.198:5000/v3',
    project_name="admin",
    username="admin",
    password="jengai8raise8Oe1",
    region_name="RegionOne",
    user_domain_name="admin_domain",
    project_domain_name="admin_domain"
)
conn.authorize()

image = conn.get_image('bionic')

# Find a flavor with at least 512M of RAM
flavor = conn.get_flavor_by_ram(512)
network = conn.get_network('60f3e830-9711-489f-b155-edead38aa1e9')

print("\n\n ...Criando \n\n")

conn.create_server(
    'server-test', image=image, flavor=flavor, wait=True, auto_ip=True, network=network)

print("\n\n...Apagando\n\n")
conn.delete_server(
    'server-test', wait=True
)

print("\n\n...Apagado!\n\n")

