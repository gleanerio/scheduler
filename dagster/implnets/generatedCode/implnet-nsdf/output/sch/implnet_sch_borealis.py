from dagster import schedule

from jobs.implnet_jobs_borealis import implnet_job_borealis

@schedule(cron_schedule="0 15 * * 1", job=implnet_job_borealis, execution_timezone="US/Central")
def implnet_sch_borealis(_context):
    run_config = {}
    return run_config
