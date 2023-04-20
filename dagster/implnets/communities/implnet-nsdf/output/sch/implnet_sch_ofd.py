from dagster import schedule

from jobs.implnet_jobs_ofd import implnet_job_ofd

@schedule(cron_schedule="0 21 * * 5", job=implnet_job_ofd, execution_timezone="US/Central")
def implnet_sch_ofd(_context):
    run_config = {}
    return run_config
