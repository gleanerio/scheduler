from dagster import schedule

from jobs.implnet_jobs_julich import implnet_job_julich

@schedule(cron_schedule="0 0 * * 5", job=implnet_job_julich, execution_timezone="US/Central")
def implnet_sch_julich(_context):
    run_config = {}
    return run_config
