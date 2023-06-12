# Configs

## Note

In addition to these config fils and the archive files.   For a full deploymnet you
need:

* The Docker compose file
* An environment file to be used with Docker among other settings this needs
    * Minio access codes
    * Portainer API key
    * Graph DB or other access code

Also:
The archive tar file generated needs to be in the Glaner Minio bucket structure located at:

GLEANERIO_GLEANER_ARCHIVE_OBJECT
GLEANERIO_GLEANER_ARCHIVE_PATH

GLEANERIO_NABU_ARCHIVE_OBJECT
GLEANERIO_NABU_ARCHIVE_PATH

in the .env file.


