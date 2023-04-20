from dagster import schedule

from jobs.implnet_jobs_rsu import implnet_job_rsu

@schedule(cron_schedule="0 18 * * 6", job=implnet_job_rsu, execution_timezone="US/Central")
def implnet_sch_rsu(_context):
    run_config = {}
    return run_config
