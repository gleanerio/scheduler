VERSION :=`cat VERSION`
   
build-oih:
	podman build  --tag="docker.io/fils/dagster_oih:$(VERSION)"  --file=./Dockerfile.oih  .

push-oih:
	podman push docker.io/fils/dagster_oih:$(VERSION) 

build-iow:
	podman build  --tag="docker.io/fils/dagster_iow:$(VERSION)"  --file=./Dockerfile.iow  .

push-iow:
	podman push docker.io/fils/dagster_iow:$(VERSION) 

