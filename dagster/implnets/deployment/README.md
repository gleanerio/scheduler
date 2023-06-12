# Deployment

## About

This file documents that elements needed for the deployment of a Dagster with Gleaner / Nabu
execution code into Docker / Portainer.

There are a set of required files:

* docker compose file
* env variables file
* archive tar file
    * containing the Gleaner or Nabu config file
    * JSON-LD context files (if needed)
    

The archive tar file is loaded, in our approach, to an object store, where the Dagster code
will retrieve it when starting new containers and load it with the archive API call.  
    

```bash
tar -zcf GleanerCfg.tgz ./gleanerconfig.yaml ./jsonldcontext.json ./assets
```

```bash
tar -zcf NabuCfg.tgz ./nabuconfig.yaml ./jsonldcontext.json ./assets  
```
