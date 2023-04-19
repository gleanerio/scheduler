# Implementation Networks

This ([https://github.com/sharmasagar25/dagster-docker-example](https://github.com/sharmasagar25/dagster-docker-example)) 
is an example on how to structure a [Dagster] project in order to organize
the jobs, repositories, schedules, and ops. The example also contains
examples on unit-tests and a docker-compose deployment file that utilizes a
Postgresql database for the run, event_log and schedule storage.

This example should in no way be considered suitable for production and is
merely my own example of a possible file structure. I personally felt that it
was difficult to put the Dagster concepts to use since the projects own examples
had widely different structure and was difficult to overview as a beginner.

The example is based on the official [tutorial].

## Folders

* build:  build directives for the docker containers
* configs
* src
* tooling

## Building the dagster code from templates

The python program pygen will read a gleaner configuration file and a set of 
template and build the Dagster code from there.  

```bash
python pygen.py -cf ./configs/nsdf/gleanerconfig.yaml -od ./src/implnet-nsdf/output  -td ./src/implnet-nsdf/templates  -d 7
```


## Running 

There is an example on how to run a single pipeline in `src/main.py`. First
install the dependencies in an isolated Python environment.

```bash
pip install -r requirements
```

The code built above can be run locally, though your templates may be set up 
to reference services and other resources not present on your dev machine.  For 
complex examples like these, it can be problematic.  

If you are looking for some simple examples of Dagster, check out the directory
examples for some smaller self-contained workflows.  There are good for testing
things like sensors and other approaches. 

If you wish to still try the generated code cd into the output directory
you specified in the pygen command.

Then use:

```bash
dagit -h ghost.lan -w workspace.yaml
```




## Building

```bash
 podman build  -t  docker.io/fils/dagster:0.0.24  .
```

```bash
 podman push docker.io/fils/dagster:0.0.24
```

## Other Examples

- [pybokeh/dagster-sklearn]
  - Gave me the inspiration for the primary folder structure. Although that
    example is more advanced and utilizes sklearn.
- [dagster-io/dagster examples]
  - Dagster's own examples.
- [xyzy-web/dagster-exchangerates]
  - An example that includes Kubernetes Deployment.
- [sephib/dagster-graph-project]
- [sspaeti-com/practical-data-engineering]

[Dagster]: https://dagster.io/
[tutorial]:https://docs.dagster.io/tutorial
[pybokeh/dagster-sklearn]: https://github.com/pybokeh/dagster-sklearn
[dagster-io/dagster examples]: https://github.com/dagster-io/dagster
[xyzy-web/dagster-exchangerates]: https://github.com/xyzy-web/dagster-exchangerates
[sephib/dagster-graph-project]: https://github.com/sephib/dagster-graph-project
[sspaeti-com/practical-data-engineering]: https://github.com/sspaeti-com/practical-data-engineering


# ScriptBuilder

## testing running

Once built you can ```cd``` into the output directory and run a command like:

```bash 
 dagit -h ghost.lan -w workspace.yaml
 ```

## About

Script to build the dagster files based on templates and a Gleaner config file.

```
sed -i  's|0 15 \* \* \*|0 1 \* \* \*|g' implnet_sch_aquadocs.py
```

We do not do assets or sensors at this time so they are not involved here.
Thy would be their oen directories in the output and then need to be 
represented in the repository.py file. 

## Cron Notes

A useful on-line tool:  [https://crontab.cronhub.io/](https://crontab.cronhub.io/)

```
0 3 * * *   is at 3 AM each day

0 3,5 * * * at 3 and 5 am each day

0 3 * * 0  at 3 am on Sunday

0 3 5 * *  At 03:00 AM, on day 5 of the month

0 3 5,19 * * At 03:00 AM, on day 5 and 19 of the month

0 3 1/4 * * At 03:00 AM, every 4 days
```
