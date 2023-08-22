
ECRR from google drive will require a manual harvest, and manual configuration.


You need to generate the code, and modify the deployed config files in s3.

pygen.py -cf ./configs/ecrr/gleanerconfig.yaml -od ./repositories/ecrr -td ./templates/v1 -d 7 

Then modify the output for the ops files

GLEANER_MINIO_BUCKET = os.environ.get('ECRR_MINIO_BUCKET')
GLEANER_GRAPH_NAMESPACE = os.environ.get('ECRR_GRAPH_NAMESPACE')

rename method gleaner in repositories/repositories.py to ecrr

Remove the gleaner, missing reporting, identifer, bucket url steps...
summarize steps.
pass some string to the first nabu step


