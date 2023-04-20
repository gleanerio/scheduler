from dagster import schedule

from jobs.implnet_jobs_dryad import implnet_job_dryad

@schedule(cron_schedule="0 12 * * 0", job=implnet_job_dryad, execution_timezone="US/Central")
def implnet_sch_dryad(_context):
    run_config = {}
    return run_config
