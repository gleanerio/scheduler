from dagster import schedule

from jobs.implnet_jobs_linked.earth import implnet_job_linked.earth

@schedule(cron_schedule="0 18 * * 0", job=implnet_job_linked.earth, execution_timezone="US/Central")
def implnet_sch_linked.earth(_context):
    run_config = {}
    return run_config
