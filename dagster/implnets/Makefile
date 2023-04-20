.ONESHELL: # Applies to every targets in the file!
.SHELLFLAGS += -e
VERSION :=`cat VERSION`

# ----  NSDF  ----

nsdf-cfgbuild:
	cd ./tooling/cfgBuilder/NSDF && python cfgBuilder.py -s https://geoconnex.us/sitemap.xml

nsdf-clean:
	cd ./generatedCode/implnet-nsdf && rm -rf ./output/*

nsdf-generate:
	python pygen.py -cf ./configs/nsdf/gleanerconfig.yaml -od ./generatedCode/implnet-nsdf/output  -td ./templates/v1   -d 7

nsdf-build:
	podman build  --tag="docker.io/fils/dagster_nsdf:$(VERSION)"  --build-arg implnet=nsdf --file=./build/Dockerfile .

nsdf-push:
	podman push docker.io/fils/dagster_nsdf:$(VERSION)

# ----  ECO  ----

eco-cfgbuild:
	cd ./tooling/cfgBuilder/ECO && python cfgBuilder.py -s https://foo.us/sitemap.xml

eco-clean:
	cd ./generatedCode/implnet-eco && rm -rf ./output/*

eco-generate:
	python pygen.py -cf ./configs/eco/gleanerconfig.yaml -od ./generatedCode/implnet-eco/output  -td ./templates/v1   -d 7

eco-build:
	podman build  --tag="docker.io/fils/dagster_eco:$(VERSION)"  --build-arg implnet=eco --file=./build/Dockerfile .

eco-push:
	podman push docker.io/fils/dagster_eco:$(VERSION)

# ----  OIH  ----

oih-cfgbuild:
	cd ./tooling/cfgBuilder/OIH && python cfgBuilder.py -s https://foo.us/sitemap.xml

oih-clean:
	cd ./generatedCode/implnet-oih && rm -rf ./output/*

oih-generate:
	python pygen.py -cf ./configs/oih/gleanerconfig.yaml -od ./generatedCode/implnet-oih/output  -td ./templates/v1   -d 7

oih-build:
	podman build  --tag="docker.io/fils/dagster_oih:$(VERSION)"  --build-arg implnet=oih --file=./build/Dockerfile .

oih-push:
	podman push docker.io/fils/dagster_oih:$(VERSION)

# ----  IoW  ----

iow-cfgbuild:
	cd ./tooling/cfgBuilder/IoW && python cfgBuilder.py -s https://foo.us/sitemap.xml

iow-clean:
	cd ./generatedCode/implnet-iow && rm -rf ./output/*

iow-generate:
	python pygen.py -cf ./configs/iow/gleanerconfig.yaml -od ./generatedCode/implnet-iow/output  -td ./templates/v1   -d 7

iow-build:
	podman build  --tag="docker.io/fils/dagster_iow:$(VERSION)"  --build-arg implnet=iow --file=./build/Dockerfile .

iow-push:
	podman push docker.io/fils/dagster_iow:$(VERSION)
