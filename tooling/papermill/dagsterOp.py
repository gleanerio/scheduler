import dagstermill as dm
from dagster._utils import script_relative_path
from dagster import job, In
from dagster import schedule

# Need 1 or N bucket name  DICT
# Need 1 or N Shape graphs  DICT
# Need 1 name to process  STR
# need 1 shape to process STR

shacl_simple = dm.define_dagstermill_op(
    "shacl_simple",
    notebook_path=script_relative_path("shacl_simple.ipynb"),
    ins={"sgurl": In(str, description="URL to the SHACL files"),
         "source_emod": In(str, description="URL to the SHACL files"),
         "sources": In(dict, description="list of numbers obtained from load_data.ipynb"),
         "shapes": In(dict, description="list of numbers obtained from load_data.ipynb")}
)

@job(
    resource_defs={
        "output_notebook_io_manager": dm.local_output_notebook_io_manager,
    }
)
def oih_validate():
    shacl_simple()
    # shacl_simple()

@schedule(cron_schedule="0 16 * * *", job=oih_validate, execution_timezone="US/Central")
def oih_sch_validation(_context):
    run_config = {}
    return run_config

