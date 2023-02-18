.ONESHELL: # Applies to every targets in the file!
.SHELLFLAGS += -e
VERSION :=`cat VERSION`

generate-oih:
	cd ./src/implnet-oih && ./generator.sh

build-oih:
	podman build  --tag="docker.io/fils/dagster_oih:$(VERSION)"  --file=./build/Dockerfile.oih  .

push-oih:
	podman push docker.io/fils/dagster_oih:$(VERSION)

generate-iow:
	cd ./src/implnet-iow && ./generator.sh

build-iow:
	podman build  --tag="docker.io/fils/dagster_iow:$(VERSION)"  --file=./build/Dockerfile.iow  .

push-iow:
	podman push docker.io/fils/dagster_iow:$(VERSION) 

generate-eco:
	cd ./src/implnet-eco && ./generator.sh

build-eco:
	podman build  --tag="docker.io/fils/dagster_eco:$(VERSION)"  --file=./build/Dockerfile.eco  .

push-eco:
	podman push docker.io/fils/dagster_eco:$(VERSION)

all-eco: generate-eco build-eco push-eco

all-oih: generate-oih build-oih push-oih

all-iow: generate-iow build-iow push-iow