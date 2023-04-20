from dagster import schedule

from jobs.implnet_jobs_iisg import implnet_job_iisg

@schedule(cron_schedule="0 9 * * 4", job=implnet_job_iisg, execution_timezone="US/Central")
def implnet_sch_iisg(_context):
    run_config = {}
    return run_config
