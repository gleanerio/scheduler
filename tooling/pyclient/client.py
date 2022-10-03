import docker

client = docker.from_env()
# client = docker.DockerClient(base_url='unix://var/run/docker.sock')

# container = client.containers.run('28_googleplay_root_x86_64:latest', name='your_name', detach=True, ports={'5556/tcp': 5556, '5555/tcp': 5555}, devices=['/dev/kvm'])
# container = client.containers.run('docker.io/library/hello-world', name='hellotest', detach=True, devices=['/dev/kvm'])

# https://docker-py.readthedocs.io/en/1.2.3/volumes/

client.containers.run("ubuntu:latest", "echo hello world")


