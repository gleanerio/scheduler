import os
import tarfile

# Code to build and deploy the needed archive files.

def lfr(directory):
    return [os.path.join(dirpath, f)
            for dirpath, dirnames, files in os.walk(directory)
            for f in files]
def create_tar_gz(files, tar_filename):
    with tarfile.open(tar_filename, 'w:gz') as tar:
        for file in files:
            tar.add(file)

def s3loader(data):
    server = os.environ.get('GLEANER_MINIO_URL') + ":" + os.environ.get('GLEANER_MINIO_PORT')
    client = Minio(
        server,
        secure=False,
        access_key=os.environ.get('GLEANER_MINIO_KEY'),
        secret_key=os.environ.get('GLEANER_MINIO_SECRET'),
    )

    # Make 'X' bucket if not exist.
    # found = client.bucket_exists("X")
    # if not found:
    #     client.make_bucket("X")
    # else:
    #     print("Bucket 'X' already exists")

    objprefix = "get from archive prefix env"
    client.put_object(os.environ.get('GLEANER_MINIO_BUCKET'),
                      objprefix,
                      io.BytesIO(data),
                      len(data))
    
    print(f"Object uploaded: {str(objprefix)}")


def main():
    print("stub for this code")
  
    ## build tar file
    files = ['README.md', './eco/gleanerconfig.yaml']
    files = lfr('./eco_archive')
    print(files)
    
    
    create_tar_gz(files, 'archive.tar.gz')

    
    ## deploy tar file
    # with open('./README.md', 'rb') as file:
    #     data = file.read()
    # 
    # s3loader(data)
    

if __name__ == '__main__':
    main()