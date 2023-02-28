.ONESHELL: # Applies to every targets in the file!
.SHELLFLAGS += -e
VERSION :=`cat VERSION`

oih-generate:
	cd ./src/implnet-oih && ./generator.sh

oih-build:
	podman build  --tag="docker.io/fils/dagster_oih:$(VERSION)"  --file=./build/Dockerfile.oih  .

oih-push:
	podman push docker.io/fils/dagster_oih:$(VERSION)

iow-cfgbuild:
	cd ./tooling/cfgBuilder/IoW && python cfgBuilder.py -s https://geoconnex.us/sitemap.xml

iow-generate:
	cd ./src/implnet-iow && ./generator.sh

iow-build:
	podman build  --tag="docker.io/fils/dagster_iow:$(VERSION)"  --file=./build/Dockerfile.iow  .

iow-push:
	podman push docker.io/fils/dagster_iow:$(VERSION) 

eco-generate:
	cd ./src/implnet-eco && ./generator.sh

eco-build:
	podman build  --tag="docker.io/fils/dagster_eco:$(VERSION)"  --file=./build/Dockerfile.eco  .

eco-push:
	podman push docker.io/fils/dagster_eco:$(VERSION)

all-eco: eco-generate eco-build eco-push

all-oih: oih-generate oih-build oih-push

all-iow: iow-generate iow-build iow-push
