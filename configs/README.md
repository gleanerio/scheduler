# Configs

## About

This diretory holds some of the general configuration files that might 
be useful for running Gleaner and Nabu.  This section is broken down
by the various communities (impementation networks).

These are provided as examples.

## TAR archive

The tar archive must be compressed and must be named to align 
with the archive ENV variable.  

```bash
 tar -zcf GleanerCfg.tgz ./gleanerconfig.yaml ./jsonldcontext.json
 ```

```bash
 tar -zcf NabuCfg.tgz ./nabuconfig.yaml ./jsonldcontext.json ./assets
```

## Environment variables

The command

```bash
source file.env
```

should set your values.  Be sure not to have spaces in 
your vars.

## Docker Compose

Example compose file for use with Dagster is included here.
It also is edited to read and express the shell variables 
into the containers.


