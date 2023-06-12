from dagster import repository
from jobs.implnet_jobs_balto import implnet_job_balto
from sch.implnet_sch_balto  import implnet_sch_balto
from jobs.implnet_jobs_neotomadb import implnet_job_neotomadb
from sch.implnet_sch_neotomadb  import implnet_sch_neotomadb
from jobs.implnet_jobs_resourceregistry import implnet_job_resourceregistry
from sch.implnet_sch_resourceregistry  import implnet_sch_resourceregistry
from jobs.implnet_jobs_unidata import implnet_job_unidata
from sch.implnet_sch_unidata  import implnet_sch_unidata
from jobs.implnet_jobs_aquadocs import implnet_job_aquadocs
from sch.implnet_sch_aquadocs  import implnet_sch_aquadocs
from jobs.implnet_jobs_iris import implnet_job_iris
from sch.implnet_sch_iris  import implnet_sch_iris
from jobs.implnet_jobs_edi import implnet_job_edi
from sch.implnet_sch_edi  import implnet_sch_edi
from jobs.implnet_jobs_bcodmo import implnet_job_bcodmo
from sch.implnet_sch_bcodmo  import implnet_sch_bcodmo
from jobs.implnet_jobs_hydroshare import implnet_job_hydroshare
from sch.implnet_sch_hydroshare  import implnet_sch_hydroshare
from jobs.implnet_jobs_iedadata import implnet_job_iedadata
from sch.implnet_sch_iedadata  import implnet_sch_iedadata
from jobs.implnet_jobs_opentopography import implnet_job_opentopography
from sch.implnet_sch_opentopography  import implnet_sch_opentopography
from jobs.implnet_jobs_unavco import implnet_job_unavco
from sch.implnet_sch_unavco  import implnet_sch_unavco
from jobs.implnet_jobs_ssdbiodp import implnet_job_ssdbiodp
from sch.implnet_sch_ssdbiodp  import implnet_sch_ssdbiodp
from jobs.implnet_jobs_linkedearth import implnet_job_linkedearth
from sch.implnet_sch_linkedearth  import implnet_sch_linkedearth
from jobs.implnet_jobs_lipdverse import implnet_job_lipdverse
from sch.implnet_sch_lipdverse  import implnet_sch_lipdverse
from jobs.implnet_jobs_ucar import implnet_job_ucar
from sch.implnet_sch_ucar  import implnet_sch_ucar
from jobs.implnet_jobs_opencoredata import implnet_job_opencoredata
from sch.implnet_sch_opencoredata  import implnet_sch_opencoredata
from jobs.implnet_jobs_magic import implnet_job_magic
from sch.implnet_sch_magic  import implnet_sch_magic
from jobs.implnet_jobs_earthchem import implnet_job_earthchem
from sch.implnet_sch_earthchem  import implnet_sch_earthchem
from jobs.implnet_jobs_xdomes import implnet_job_xdomes
from sch.implnet_sch_xdomes  import implnet_sch_xdomes
from jobs.implnet_jobs_neon import implnet_job_neon
from sch.implnet_sch_neon  import implnet_sch_neon
from jobs.implnet_jobs_designsafe import implnet_job_designsafe
from sch.implnet_sch_designsafe  import implnet_sch_designsafe
from jobs.implnet_jobs_r2r import implnet_job_r2r
from sch.implnet_sch_r2r  import implnet_sch_r2r
from jobs.implnet_jobs_geocodes_demo_datasets import implnet_job_geocodes_demo_datasets
from sch.implnet_sch_geocodes_demo_datasets  import implnet_sch_geocodes_demo_datasets
from jobs.implnet_jobs_usapdc import implnet_job_usapdc
from sch.implnet_sch_usapdc  import implnet_sch_usapdc
from jobs.implnet_jobs_cchdo import implnet_job_cchdo
from sch.implnet_sch_cchdo  import implnet_sch_cchdo
from jobs.implnet_jobs_amgeo import implnet_job_amgeo
from sch.implnet_sch_amgeo  import implnet_sch_amgeo
 
@repository
def gleaner():
	jobs = [implnet_job_balto, implnet_job_neotomadb, implnet_job_resourceregistry, implnet_job_unidata, implnet_job_aquadocs, implnet_job_iris, implnet_job_edi, implnet_job_bcodmo, implnet_job_hydroshare, implnet_job_iedadata, implnet_job_opentopography, implnet_job_unavco, implnet_job_ssdbiodp, implnet_job_linkedearth, implnet_job_lipdverse, implnet_job_ucar, implnet_job_opencoredata, implnet_job_magic, implnet_job_earthchem, implnet_job_xdomes, implnet_job_neon, implnet_job_designsafe, implnet_job_r2r, implnet_job_geocodes_demo_datasets, implnet_job_usapdc, implnet_job_cchdo, implnet_job_amgeo]
	schedules = [implnet_sch_balto, implnet_sch_neotomadb, implnet_sch_resourceregistry, implnet_sch_unidata, implnet_sch_aquadocs, implnet_sch_iris, implnet_sch_edi, implnet_sch_bcodmo, implnet_sch_hydroshare, implnet_sch_iedadata, implnet_sch_opentopography, implnet_sch_unavco, implnet_sch_ssdbiodp, implnet_sch_linkedearth, implnet_sch_lipdverse, implnet_sch_ucar, implnet_sch_opencoredata, implnet_sch_magic, implnet_sch_earthchem, implnet_sch_xdomes, implnet_sch_neon, implnet_sch_designsafe, implnet_sch_r2r, implnet_sch_geocodes_demo_datasets, implnet_sch_usapdc, implnet_sch_cchdo, implnet_sch_amgeo]

 
	return jobs + schedules
