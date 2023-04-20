from dagster import schedule

from jobs.implnet_jobs_pesquisa import implnet_job_pesquisa

@schedule(cron_schedule="0 15 * * 6", job=implnet_job_pesquisa, execution_timezone="US/Central")
def implnet_sch_pesquisa(_context):
    run_config = {}
    return run_config
