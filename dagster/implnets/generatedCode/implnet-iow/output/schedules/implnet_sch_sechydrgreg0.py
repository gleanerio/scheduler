from dagster import schedule

from jobs.implnet_jobs_sechydrgreg0 import implnet_job_sechydrgreg0

@schedule(cron_schedule="0 6 * * 1", job=implnet_job_sechydrgreg0, execution_timezone="US/Central")
def implnet_sch_sechydrgreg0(_context):
    run_config = {}
    return run_config
