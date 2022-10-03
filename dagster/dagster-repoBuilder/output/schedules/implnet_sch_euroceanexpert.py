from dagster import schedule

from gleaner.jobs.implnet_jobs_euroceanexpert import implnet_job_euroceanexpert

@schedule(cron_schedule="0 15 * * 0", job=implnet_job_euroceanexpert, execution_timezone="US/Central")
def implnet_sch_euroceanexpert(_context):
    run_config = {}
    return run_config
