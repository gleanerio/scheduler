import dagstermill as dm
from dagster._utils import script_relative_path
from dagster import job, In
from dagster import schedule



# @op(
    # config_schema={
        # "sgurl": str,
    # }
# )
# def shacl_simple(context):
    # dm.define_dagstermill_op( "shacl_simple", script_relative_path("./shacl_simple.ipynb"), output_notebook_name="dagster_output")
    # ins={"sgurl": In(str, description="URL to the SHACL files")}


# @op(config_schema={"sgurl": str})
# def op_using_config(context):
    # return f'hello {context.op_config["person_name"]}'


# @asset(config_schema={"sgurl": str})
# def asset_using_config(context):
    # # Note how asset config is also accessed with context.op_config
    # return f'hello {context.op_config["person_name"]}'

# @resource(config_schema={"sgurl": str})
# def resource_using_config(context):
    # return shacl_simple(context.resource_config["sgurl"])

# @configured(shacl_simple)
# def shacl1_session(_init_context):
    # return {"sgurl": "https://raw.githubusercontent.com/iodepo/odis-arch/schema-dev-df/code/notebooks/validation/shapes/oih_search.ttl"}

# shacl_simple = dm.define_dagstermill_op(
    # "shacl_simple",
    # script_relative_path("./shacl_simple.ipynb"),
    # output_notebook_name="dagster_output",
    # #ins={"sgurl": In(str, description="URL to the SHACL files")},
# )

shacl_simple = dm.define_dagstermill_op(
    # Name of the op:
    "shacl_simple",
    # Path to the notebook
    notebook_path=script_relative_path("shacl_simple.ipynb"),
    # The op's inputs.
    # ins={"numbers": In(list, description="list of numbers obtained from load_data.ipynb")}
    ins={"sgurl": In(str, description="URL to the SHACL files")}
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

