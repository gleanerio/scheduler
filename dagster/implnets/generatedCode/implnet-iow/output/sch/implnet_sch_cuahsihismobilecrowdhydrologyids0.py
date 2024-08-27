from dagster import schedule

from jobs.implnet_jobs_cuahsihismobilecrowdhydrologyids0 import implnet_job_cuahsihismobilecrowdhydrologyids0

@schedule(cron_schedule="0 0 1 * *", job=implnet_job_cuahsihismobilecrowdhydrologyids0, execution_timezone="US/Central")
def implnet_sch_cuahsihismobilecrowdhydrologyids0(_context):
    run_config = {}
    return run_config
