# thoughs on how to make sources and sensors dynamic.

Config thoughts:
idea 1
* sources as a singlefil
* communities just have a list of source names
idea 2
* a community a source list. with some community properties (name,)
* we grab all community sources, merge them, then build schedules.

In  the module init:
* create a method that creates schedules, for list of sources.
* creat a method that creates sensors for a list of tennant configurations

# seonsor example:
Create sensor as job
https://github.com/dagster-io/dagster/blob/2285c96f07cc153c1e6331840c3d55df61251663/examples/project_fully_featured/project_fully_featured/jobs.py#L7
Function to creeate sensor
https://github.com/dagster-io/dagster/blob/master/examples/project_fully_featured/project_fully_featured/sensors/hn_tables_updated_sensor.py
add to __init.py__
https://github.com/dagster-io/dagster/blob/2285c96f07cc153c1e6331840c3d55df61251663/examples/project_fully_featured/project_fully_featured/__init__.py#L34

Start with one. Figure out how to do multiple with different tennants.

# scheudle

* read a file with the sources. Mount in container using config. No secrets in file.
   * maybe use a url file:// so that we might be able to put into an s3 bucket.
* method to create a schedule definigition for each source. return array of schedules
* add to __init__.py definition in schedules.

This requires on configuration to load to a single s3.


dynamic partitions
https://docs.dagster.io/concepts/partitions-schedules-sensors/partitioning-assets#dynamically-partitioned-assets
