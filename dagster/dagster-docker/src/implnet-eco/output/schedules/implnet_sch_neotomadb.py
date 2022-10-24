from dagster import schedule

from jobs.implnet_jobs_neotomadb import implnet_job_neotomadb

@schedule(cron_schedule="0 1 * * 0", job=implnet_job_neotomadb, execution_timezone="US/Central")
def implnet_sch_neotomadb(_context):
    run_config = {}
    return run_config
