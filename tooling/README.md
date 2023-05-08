# Tool Documentation

## About

These are just some utility tools related to some aspects of generating and 
checking Gleaner config files and sitemap.xml documents.  These tools are not 
critical and are only here for reference.

The main approach in this repo as a whole is really based around the 
pre-requisite of have a valid Gleaner Configuration file already.  

So these tools might be of interest only if you are still working toward 
that goal. 

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
 
