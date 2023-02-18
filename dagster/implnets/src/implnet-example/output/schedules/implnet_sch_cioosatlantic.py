from dagster import schedule

from jobs.implnet_jobs_cioosatlantic import implnet_job_cioosatlantic

@schedule(cron_schedule="0 18 * * 0", job=implnet_job_cioosatlantic, execution_timezone="US/Central")
def implnet_sch_cioosatlantic(_context):
    run_config = {}
    return run_config
