# refactoring

## rework code to generate less.
* ~~just generate the graph, and some configuration loading~~ done
* ~~pass the ops the configuration~~

## can we use s3 manager to store some assets?
* ~~reports seems like the ideal use case for these.~~ works

## handle multiple workflows
* ~~need to add ability to deploy some other workflows~~ works


### Handle Multiple Organizations
* Each organization can be in a container with its own code workflow.
* If we can standardize the loading and transforming workflows as much as possible, then the graph loading workflows 
 should be more customizable
* to add a container, you need to edit the workflows.yaml in an organizations configuration
  
### possible workflows
* ~~timeseries after final graph~~ done
    * ~~generate a csv of the load reports size of (sitemap, summoned, summon failure, milled, loaded to graph, datasets)~~

* ~~weekly summary~~ done
    *  ~~what is the size of the graph this week.~~
* post s3 check, as an approval check. 
    * do these not contain JSONLD
    * store as asset, or maybe have file we publish as 'approved/expected non-summoned
* sitemap check
    * just run a sitemap head to see that url work, and exist, weekly.
    * publish as paritioned data in s3 ;)
* shacl... should we shacl releases.
    * if so, then maybe teach dagster to watch the graph/latest for changes.
