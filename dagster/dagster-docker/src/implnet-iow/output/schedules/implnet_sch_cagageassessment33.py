from dagster import schedule

from jobs.implnet_jobs_cagageassessment33 import implnet_job_cagageassessment33

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cagageassessment33, execution_timezone="US/Central")
def implnet_sch_cagageassessment33(_context):
    run_config = {}
    return run_config
