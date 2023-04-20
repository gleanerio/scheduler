from dagster import schedule

from jobs.implnet_jobs_abacus import implnet_job_abacus

@schedule(cron_schedule="0 0 * * 1", job=implnet_job_abacus, execution_timezone="US/Central")
def implnet_sch_abacus(_context):
    run_config = {}
    return run_config
