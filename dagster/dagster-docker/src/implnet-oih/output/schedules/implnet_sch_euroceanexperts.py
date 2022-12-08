from dagster import schedule

from jobs.implnet_jobs_euroceanexperts import implnet_job_euroceanexperts

@schedule(cron_schedule="0 18 * * 1", job=implnet_job_euroceanexperts, execution_timezone="US/Central")
def implnet_sch_euroceanexperts(_context):
    run_config = {}
    return run_config
