from dagster import schedule

from jobs.implnet_jobs_earthchem import implnet_job_earthchem

@schedule(cron_schedule="0 12 2 * *", job=implnet_job_earthchem, execution_timezone="US/Central")
def implnet_sch_earthchem(_context):
    run_config = {}
    return run_config
