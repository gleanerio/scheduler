import papermill as pm

pm.execute_notebook(
        '../shacl_simple.ipynb',
        './output.ipynb',
        parameters = dict(dg="https://raw.githubusercontent.com/geoschemas-org/geoshapes/master/datagraphs/dataset-full-BAD.json-ld",
            sgurl="https://raw.githubusercontent.com/ESIPFed/science-on-schema.org/master/validation/shapegraphs/soso_common_v1.2.3.ttl"))
