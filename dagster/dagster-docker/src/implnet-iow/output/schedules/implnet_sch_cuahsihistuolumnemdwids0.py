from dagster import schedule

from jobs.implnet_jobs_cuahsihistuolumnemdwids0 import implnet_job_cuahsihistuolumnemdwids0

@schedule(cron_schedule="0 21 * * 0", job=implnet_job_cuahsihistuolumnemdwids0, execution_timezone="US/Central")
def implnet_sch_cuahsihistuolumnemdwids0(_context):
    run_config = {}
    return run_config
