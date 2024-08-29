.ONESHELL: # Applies to every targets in the file!
.SHELLFLAGS += -e
VERSION :=`cat VERSION`

CONFIG = iow

nsdf-generate:
	cd ./dagster/implnets; python pygen.py -cf ./dagster/implnets/configs/nsdf/gleanerconfig.yaml -od ./dagster/implnets/generatedCode/implnet-nsdf/output  -td ./dagster/implnets/templates/v1   -d 7

oih-generate:
	cd ./dagster/implnets; python pygen.py -cf ./dagster/implnets/configs/oih/gleanerconfig.yaml -od ./dagster/implnets/generatedCode/implnet-oih/output  -td ./dagster/implnets/templates/v1   -d 14

oih-build:
	podman push docker.io/fils/dagster_oih:$(VERSION)


clean:
	@echo "Cleaning contents of the build directory"
	@find ./build -mindepth 1 ! -name '.gitkeep' -exec rm -rf {} +

cfgbuild:
	cd ./tooling/cfgBuilder/$(CONFIG) && python cfgBuilder.py -s https://geoconnex.us/sitemap.xml

generate: 
	cd ./dagster/implnets; python pygen.py -cf ../../build/gleanerconfig.yaml -od ../../build -td ./templates/v1   -d 27

build:
	podman build  --tag="docker.io/fils/dagster_$(CONFIG):$(VERSION)"  --build-arg implnet=$(CONFIG) --file=./dagster/implnets/build/Dockerfile .

push:
	podman push docker.io/fils/dagster_$(CONFIG):$(VERSION)
