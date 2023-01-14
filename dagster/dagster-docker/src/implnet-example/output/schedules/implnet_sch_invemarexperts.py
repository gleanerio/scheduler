from dagster import schedule

from jobs.implnet_jobs_invemarexperts import implnet_job_invemarexperts

@schedule(cron_schedule="0 0 * * 4", job=implnet_job_invemarexperts, execution_timezone="US/Central")
def implnet_sch_invemarexperts(_context):
    run_config = {}
    return run_config
