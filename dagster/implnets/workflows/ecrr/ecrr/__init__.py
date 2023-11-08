from dagster import repository, Definitions

from .jobs.implnet_jobs_ecrr_submitted import job_ecrr_submitted
from .sch.implnet_sch_ecrr_submitted  import implnet_sch_ecrr_submitted
from .jobs.implnet_jobs_ecrr_examples import job_ecrr_examples
from .sch.implnet_sch_ecrr_examples  import implnet_sch_ecrr_examples


jobs = [ job_ecrr_submitted, job_ecrr_examples]
schedules = [ implnet_sch_ecrr_submitted, implnet_sch_ecrr_examples]

defs = Definitions(
	jobs=jobs,
	schedules=schedules,
)
