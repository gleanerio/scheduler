# Scheduler Documentation

## Simple Flow

1. run sourcesToCfg.py with config saved to x/y/z

```
python sourcesToCfg.py -o ../../../dagster/dagster-docker/bin/implnet_oih/gleanerconfig.yaml -s https://raw.githubusercontent.com/iodepo/odis-arch/master/config/sources.yaml
```
In the first step above the config file should be output to implementation path
like:

```
.../scheduler/dagster/dagster-docker/bin/implnet_oih/gleanerconfig.yaml
```

2. OPTIONAL use sitemap checker

```
python check_sitemap_loop.py --source=https://raw.githubusercontent.com/iodepo/odis-arch/master/config/sources.yaml  --name=obis
```

From there it can be used in the next steps.

3. from .../dagster/dagster-docker/src/implnet-oih run generator.sh with the
path to the config file:

```
./generator.sh ../../bin/implnet_oih/gleanerconfig.yaml
```

4. Build the images (increment VERSION) and push out the containers.

At this point the new images can be pushed out to an orchestration environment.

