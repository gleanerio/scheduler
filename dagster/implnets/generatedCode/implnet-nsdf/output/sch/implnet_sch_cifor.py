from dagster import schedule

from jobs.implnet_jobs_cifor import implnet_job_cifor

@schedule(cron_schedule="0 18 * * 1", job=implnet_job_cifor, execution_timezone="US/Central")
def implnet_sch_cifor(_context):
    run_config = {}
    return run_config
