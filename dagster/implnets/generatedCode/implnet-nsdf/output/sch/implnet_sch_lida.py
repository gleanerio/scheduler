from dagster import schedule

from jobs.implnet_jobs_lida import implnet_job_lida

@schedule(cron_schedule="0 9 * * 5", job=implnet_job_lida, execution_timezone="US/Central")
def implnet_sch_lida(_context):
    run_config = {}
    return run_config
