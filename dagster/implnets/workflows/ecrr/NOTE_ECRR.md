TESTING UPLOADING WITH LOAD:
LOAD <https://oss.geocodes-aws-dev.earthcube.org/ecrr/graphs/latest/ecrr_examples_release.nq>
LOAD <https://oss.geocodes-aws-dev.earthcube.org/ecrr/graphs/latest/ecrr_submitted_release.nq>


ECRR from google drive will require a manual harvest, and manual configuration.

ECRR_SUMBITTED IS THE REPO TO LOAD.

ECRR_EXAMPLES is a sitemap from the GecodesMetadata repository

It will not need to be summoned. It will be rsyc'd from the old goodge drive for now, and 
later, it will need to read from the s3 bucket where the files are stored by the JSONFORMS app.


You need to generate the code, and modify the deployed config files in s3.

pygen.py -cf ./configs/ecrr/gleanerconfig.yaml -od ./workflows/generated/ecrr -td ./templates/v1 -d 7 

Then modify the output for the ops files and put into the ecrr folder.


GLEANER_MINIO_BUCKET = os.environ.get('ECRR_MINIO_BUCKET')
GLEANER_GRAPH_NAMESPACE = os.environ.get('ECRR_GRAPH_NAMESPACE')

rename method gleaner in repositories/repositories.py to ecrr

Remove the gleaner, missing reporting, identifer, bucket url steps...
summarize steps.
pass some string to the first nabu step

# RUNNING LOCALLY
* You need to point at a docker STACK, or portainer endpoint... A local workstation docker is usually not a STACK.
* set the ENV variables; ECRR_MINIO_BUCKET ECRR_GRAPH_NAMESPACE
* 
`cd workflows/ecrr/ecrr
python -m dagster dev `

To run a job:
`cd workflows/ecrr/ecrr
python -m dagster job execute -f jobs/implnet_jobs_ecrr_examples.py  -j implnet_job_ecrr_examples`
