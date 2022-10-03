from dagster import schedule

from jobs.implnet_jobs_invemarvessel import implnet_job_invemarvessel

@schedule(cron_schedule="0 6 * * 0", job=implnet_job_invemarvessel, execution_timezone="US/Central")
def implnet_sch_invemarvessel(_context):
    run_config = {}
    return run_config
