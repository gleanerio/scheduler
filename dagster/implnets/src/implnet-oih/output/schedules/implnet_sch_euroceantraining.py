from dagster import schedule

from jobs.implnet_jobs_euroceantraining import implnet_job_euroceantraining

@schedule(cron_schedule="0 18 * * 2", job=implnet_job_euroceantraining, execution_timezone="US/Central")
def implnet_sch_euroceantraining(_context):
    run_config = {}
    return run_config
