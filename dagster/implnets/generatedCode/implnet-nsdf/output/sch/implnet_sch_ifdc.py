from dagster import schedule

from jobs.implnet_jobs_ifdc import implnet_job_ifdc

@schedule(cron_schedule="0 3 * * 4", job=implnet_job_ifdc, execution_timezone="US/Central")
def implnet_sch_ifdc(_context):
    run_config = {}
    return run_config
