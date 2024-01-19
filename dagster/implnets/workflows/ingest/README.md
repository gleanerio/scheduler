# Ingest Rework

This is an attempt to rework the ingest system, to split the summon/release file from the load to graph 
and clean graph, and the reporting.


## gleaner io container routines
* summon : run gleaner, run nabu release
   * assets -> summon path (metadata: s3:path file count, time), release file (metadata: s3path, size, time), reports
* relase
* prune
* prov
* orgs

##  ops:
  * Load to graph
  * summarize
  * load summarize
  * reports
  * graph (prune, prov, orgs)
  * community stats
  * UI
## Sensor:
These routines are useful to all communities.

* new release file 
   * run prov
   * run bucket report, missing report, identifier report 
   * run summarize. Not needed by all communiities, but prevents duplicate op from being run. Can add a flag.

# Sensor for a community
Have a sensor that looks at the release files, and then determines if a release needs to be pushed to a communit
if this release is a source in my community.
   * load graph
     * graph report 
   * load prov
   * load summarize
   * (ec) run community stats (about)



This is a [Dagster](https://dagster.io/) project made to be used alongside the official [Dagster tutorial](https://docs.dagster.io/tutorial).

Use Dagster AWS for minio configuraiton
