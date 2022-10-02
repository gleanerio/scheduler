from dagster import schedule

from gleaner.jobs.implnet_jobs_nodcid import implnet_job_nodcid

@schedule(cron_schedule="0 16 * * *", job=implnet_job_nodcid, execution_timezone="US/Central")
def implnet_sch_nodcid(_context):
    run_config = {}
    return run_config
