from dagster import schedule

from jobs.implnet_jobs_asulrdr import implnet_job_asulrdr

@schedule(cron_schedule="0 9 * * 1", job=implnet_job_asulrdr, execution_timezone="US/Central")
def implnet_sch_asulrdr(_context):
    run_config = {}
    return run_config
