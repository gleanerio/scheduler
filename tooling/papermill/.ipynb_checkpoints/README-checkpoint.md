# Papermill notes

## Usage

### Gleaner

For examples used in this repository we are using the command line approach in this manner.
The associated YAML file values could alternatively be provided on the command line. Also
the _-k python3_ is needed to address issues with running papermill in an environment where
conda envs are used.  

```
papermill ../shacl_simple.ipynb output.ipynb -f params.yml -k python3
```

### Parameterizing a Notebook

To parameterize your notebook designate a cell with the tag ``parameters``.

![enable parameters in Jupyter](docs/img/enable_parameters.gif)

Papermill looks for the ``parameters`` cell and treats this cell as defaults for the parameters passed in at execution time. Papermill will add a new cell tagged with ``injected-parameters`` with input parameters in order to overwrite the values in ``parameters``. If no cell is tagged with ``parameters`` the injected cell will be inserted at the top of the notebook.

Additionally, if you rerun notebooks through papermill and it will reuse the ``injected-parameters`` cell from the prior run. In this case Papermill will replace the old ``injected-parameters`` cell with the new run's inputs.

![image](docs/img/parameters.png)

### Executing a Notebook

The two ways to execute the notebook with parameters are: (1) through
the Python API and (2) through the command line interface.

#### Execute via the Python API

``` {.sourceCode .python}
import papermill as pm

pm.execute_notebook(
   'path/to/input.ipynb',
      'path/to/output.ipynb',
         parameters = dict(alpha=0.6, ratio=0.1)
         
        )
`````

#### Execute via CLI

Here's an example of a local notebook being executed and output to an
Amazon S3 account:

``` {.sourceCode .bash}
$ papermill local/input.ipynb s3://bkt/output.ipynb -p alpha 0.6 -p l1_ratio 0.1
`````````
````
