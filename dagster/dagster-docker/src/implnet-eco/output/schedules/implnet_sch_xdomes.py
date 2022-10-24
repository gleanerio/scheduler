from dagster import schedule

from jobs.implnet_jobs_xdomes import implnet_job_xdomes

@schedule(cron_schedule="0 2 * * 0", job=implnet_job_xdomes, execution_timezone="US/Central")
def implnet_sch_xdomes(_context):
    run_config = {}
    return run_config
