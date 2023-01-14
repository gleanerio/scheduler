from dagster import schedule

from jobs.implnet_jobs_oceanscape import implnet_job_oceanscape

@schedule(cron_schedule="0 6 * * 6", job=implnet_job_oceanscape, execution_timezone="US/Central")
def implnet_sch_oceanscape(_context):
    run_config = {}
    return run_config
