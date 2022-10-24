from dagster import schedule

from jobs.implnet_jobs_usap-dc import implnet_job_usap-dc

@schedule(cron_schedule="0 7 * * 0", job=implnet_job_usap-dc, execution_timezone="US/Central")
def implnet_sch_usap-dc(_context):
    run_config = {}
    return run_config
