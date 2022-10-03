import docker

# https://docker-py.readthedocs.io/en/stable/containers.html

client = docker.from_env()
client = docker.DockerClient(base_url='unix://var/run/docker.sock')

# container = client.containers.run('28_googleplay_root_x86_64:latest', name='your_name', detach=True, ports={'5556/tcp': 5556, '5555/tcp': 5555}, devices=['/dev/kvm'])
# container = client.containers.run('docker.io/library/hello-world', name='hellotest', detach=True, devices=['/dev/kvm'])
# returned_value = client.containers.run('docker.io/fils/nabu:2.0.3-developement'  '--cfg /oihlocal.yaml  prune -s summoned/aquadocs')

# REF: # https://docker-py.readthedocs.io/en/1.2.3/volumes/
container_id = client.create_container(
    'docker.io/fils/nabu:2.0.3-developement', 'prune --cfg /oihlocal.yaml  -s summoned/aquadocs',
    volumes=['/nabu/config'],
    host_config=docker.utils.create_host_config(binds={
        '/home/user1/tmp/nabu': {
            'bind': '/nabu/config',
            'ro': False
        }
    })
)

t = container_id.run("docker.io/fils/nabu:2.0.3-developement",  "prune --cfg oihlocal.yaml  -s summoned/aquadocs")
print(t)

#x = client.containers.run("docker.io/fils/nabu:2.0.3-developement")
# x = client.containers.run("docker.io/fils/nabu:2.0.3-developement",  "-help")
x = client.containers.run("docker.io/fils/nabu:2.0.3-developement",  "prune --cfg oihlocal.yaml  -s summoned/aquadocs")
print(x)

# x = client.containers.run("ubuntu:latest", "echo hello world")
# print(x)
