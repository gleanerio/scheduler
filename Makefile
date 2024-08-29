.ONESHELL: # Applies to every targets in the file!
.SHELLFLAGS += -e
VERSION :=`cat VERSION`

# ----  ECO  ----

eco-cfgbuild:
	cd ./dagster/implnets/tooling/cfgBuilder/ECO && python cfgBuilder.py -s https://foo.us/sitemap.xml

eco-clean:
	cd ./dagster/implnets/generatedCode/implnet-eco && rm -rf ./dagster/implnets/output/*

eco-generate:
	python3 pygen.py -cf ./dagster/implnets/configs/eco/gleanerconfig.yaml -od ./dagster/implnets/generatedCode/implnet-eco/output  -td ./dagster/implnets/templates/v1   -d 7

eco-build:
	podman build  --tag="docker.io/fils/dagster_eco:$(VERSION)"  --build-arg implnet=eco --file=./dagster/implnets/build/Dockerfile .

eco-push:
	podman push docker.io/fils/dagster_eco:$(VERSION)


# ----  NSDF  ----

nsdf-cfgbuild:
	cd ./dagster/implnets/tooling/cfgBuilder/NSDF && python cfgBuilder.py -s https://geoconnex.us/sitemap.xml

nsdf-clean:
	cd ./dagster/implnets/generatedCode/implnet-nsdf && rm -rf ./dagster/implnets/output/*

nsdf-generate:
	cd ./dagster/implnets; python pygen.py -cf ./dagster/implnets/configs/nsdf/gleanerconfig.yaml -od ./dagster/implnets/generatedCode/implnet-nsdf/output  -td ./dagster/implnets/templates/v1   -d 7

nsdf-build:
	podman build  --tag="docker.io/fils/dagster_nsdf:$(VERSION)"  --build-arg implnet=nsdf --file=./dagster/implnets/build/Dockerfile .

nsdf-push:
	podman push docker.io/fils/dagster_nsdf:$(VERSION)

# ----  OIH  ----

oih-cfgbuild:
	cd ./dagster/implnets/tooling/cfgBuilder/OIH && python cfgBuilder.py -s https://foo.us/sitemap.xml

oih-clean:
	cd ./dagster/implnets/generatedCode/implnet-oih && rm -rf ./dagster/implnets/output/*

oih-generate:
	cd ./dagster/implnets; python pygen.py -cf ./dagster/implnets/configs/oih/gleanerconfig.yaml -od ./dagster/implnets/generatedCode/implnet-oih/output  -td ./dagster/implnets/templates/v1   -d 14

oih-build:
	podman build  --tag="docker.io/fils/dagster_oih:$(VERSION)"  --build-arg implnet=oih --file=./dagster/implnets/build/Dockerfile .

oih-push:
	podman push docker.io/fils/dagster_oih:$(VERSION)

# ----  IoW  ----

iow-cfgbuild:
	cd ./tooling/cfgBuilder/iow && python cfgBuilder.py -s https://geoconnex.us/sitemap.xml

iow-clean:
	@echo "Cleaning contents of the build directory"
	@find ./build -mindepth 1 ! -name '.gitkeep' -exec rm -rf {} +

iow-generate:
	cd ./dagster/implnets; python pygen.py -cf ./configs/iow/gleanerconfig.yaml -od ../../build -td ./templates/v1   -d 27

iow-build:
	podman build  --tag="docker.io/fils/dagster_iow:$(VERSION)"  --build-arg implnet=iow --file=./dagster/implnets/build/Dockerfile .

iow-push:
	podman push docker.io/fils/dagster_iow:$(VERSION)
