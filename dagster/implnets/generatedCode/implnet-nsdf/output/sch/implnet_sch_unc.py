from dagster import schedule

from jobs.implnet_jobs_unc import implnet_job_unc

@schedule(cron_schedule="0 6 * * 0", job=implnet_job_unc, execution_timezone="US/Central")
def implnet_sch_unc(_context):
    run_config = {}
    return run_config
