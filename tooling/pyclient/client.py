:wheelimport docker

client = docker.from_env()
client = docker.DockerClient(base_url='unix://var/run/docker.sock')

# container = client.containers.run('28_googleplay_root_x86_64:latest', name='your_name', detach=True, ports={'5556/tcp': 5556, '5555/tcp': 5555}, devices=['/dev/kvm'])
# container = client.containers.run('docker.io/library/hello-world', name='hellotest', detach=True, devices=['/dev/kvm'])

# https://docker-py.readthedocs.io/en/1.2.3/volumes/

# returned_value = client.containers.run('docker.io/fils/nabu:2.0.3-developement'  '--cfg /oihlocal.yaml  prune -s summoned/aquadocs')

x = client.containers.run("docker.io/fils/nabu:2.0.3-developement",  "prune --cfg oihlocal.yaml  -s summoned/aquadocs")
print(x)

# x = client.containers.run("ubuntu:latest", "echo hello world")
# print(x)

# exec podman run  --privileged   --network=host   --interactive --tty --rm   --volume "$PWD":/nabu/wd     --workdir /nabu/wd  "docker.io/fils/nabu:2.0.3-developement" "$@"

# container_id = c.create_container(
#     'busybox', 'ls', volumes=['/mnt/vol1', '/mnt/vol2'],
#     host_config=docker.utils.create_host_config(binds={
#         '/home/user1/': {
#             'bind': '/mnt/vol2',
#             'ro': False
#         },
#         '/var/www': {
#             'bind': '/mnt/vol1',
#             'ro': True
#         }
#     })
# )




