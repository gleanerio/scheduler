import docker

# https://docker-py.readthedocs.io/en/stable/containers.html
# https://stackoverflow.com/questions/50368466/how-can-i-mount-a-file-into-a-directory-in-a-docker-container-using-docker-py
# REF: # https://docker-py.readthedocs.io/en/1.2.3/volumes/
# https://stackoverflow.com/questions/54688176/python-docker-how-to-mount-the-directory-from-host-to-container

# client = docker.from_env()
client = docker.DockerClient(base_url='unix://var/run/docker.sock')

# os.getcwd():
# stdout = client.containers.run(
#     image='docker.io/fils/nabu:2.0.3-developement',
#     name='nabu',
#     volumes={
#         '/nabu/config/oihlocal.yaml': {
#             'bind': '/home/fils/src/Projects/gleaner.io/scheduler/tooling/dockerPyclient/naburundir/oihlocal.yaml',
#             'mode': 'rw',
#         }
#     },
#     # network='host',
#     command='prune --cfg /nabu/config/oihlocal.yaml  -s summoned/aquadocs',
# )
# print(stdout.logs())

#x = client.containers.run("docker.io/fils/nabu:2.0.3-developement")
# x = client.containers.run("docker.io/fils/nabu:2.0.3-developement",  "-help")
# x = client.containers.run("docker.io/fils/nabu:2.0.3-developement",  "prune --cfg oihlocal.yaml  -s summoned/aquadocs")
# print(x)

x = client.containers.run("ubuntu:latest", "echo hello world")
print(x)

# MORGUE
# container = client.containers.run('28_googleplay_root_x86_64:latest', name='your_name', detach=True, ports={'5556/tcp': 5556, '5555/tcp': 5555}, devices=['/dev/kvm'])
# container = client.containers.run('docker.io/library/hello-world', name='hellotest', detach=True, devices=['/dev/kvm'])
# returned_value = client.containers.run('docker.io/fils/nabu:2.0.3-developement'  '--cfg /oihlocal.yaml  prune -s summoned/aquadocs')

