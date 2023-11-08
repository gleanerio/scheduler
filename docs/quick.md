# Notes

## Implementation network builder

The work for building the dagster containers for a given implementation network starts in 
the directory ```scheduler/dagster/implnets```.  At this time most of this can be driven by
the Makefile.

??? Note
   github actions build containers to [nsfearthcube](https://hub.docker.com/?namespace=nsfearthcube)
   so the below is about deploying manually

1) Make sure your gleanerconfig.yaml file is in the configs/PROJECT directory where
   PROJECT is your implmentation network like eco, iow, etc.
2) Check the VERSION file and make sure it has a value you want in it to be tagged to the containers.
3) ```make eco-clean```  will remove any existing generated code from the ./generatedCode/implnet-NETWORK directory
4) ```make eco-generate``` will build the code new.  Set the -d N in the makefile to a value N that is the number
   of days you want the runs to cycle over.  So 30 would mean they run once every 30 days.  If you want some providers
   to index at different rates you currently need to go in and edit the associated provider _schedules_ file editing the
   line ```@schedule(cron_schedule="0 12 * * 6", job=implnet_job_amgeo, execution_timezone="US/Central")``` with a 
   cron value you want.
5) ```make eco-build``` builds the Docker images following the build file ./build/Docker file.  Note this uses the 
   command line argument ```--build-arg implnet=eco``` to set the implementation NETWORK so that the correct build code 
   from _generatedCode/NETWORK_ is copied over
6) ```make eco-push``` push to your container registry of choice, here docker.io



