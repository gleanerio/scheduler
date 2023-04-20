from dagster import schedule

from jobs.implnet_jobs_fiu import implnet_job_fiu

@schedule(cron_schedule="0 9 * * 3", job=implnet_job_fiu, execution_timezone="US/Central")
def implnet_sch_fiu(_context):
    run_config = {}
    return run_config
