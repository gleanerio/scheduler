from dagster import repository
from jobs.implnet_jobs_arecibo import implnet_job_arecibo
from sch.implnet_sch_arecibo  import implnet_sch_arecibo
from jobs.implnet_jobs_aws import implnet_job_aws
from sch.implnet_sch_aws  import implnet_sch_aws
from jobs.implnet_jobs_cyvers import implnet_job_cyvers
from sch.implnet_sch_cyvers  import implnet_sch_cyvers
from jobs.implnet_jobs_drp import implnet_job_drp
from sch.implnet_sch_drp  import implnet_sch_drp
from jobs.implnet_jobs_dryad import implnet_job_dryad
from sch.implnet_sch_dryad  import implnet_sch_dryad
from jobs.implnet_jobs_matcommons import implnet_job_matcommons
from sch.implnet_sch_matcommons  import implnet_sch_matcommons
from jobs.implnet_jobs_mdf import implnet_job_mdf
from sch.implnet_sch_mdf  import implnet_sch_mdf
from jobs.implnet_jobs_neon import implnet_job_neon
from sch.implnet_sch_neon  import implnet_sch_neon
from jobs.implnet_jobs_abacus import implnet_job_abacus
from sch.implnet_sch_abacus  import implnet_sch_abacus
from jobs.implnet_jobs_acss import implnet_job_acss
from sch.implnet_sch_acss  import implnet_sch_acss
from jobs.implnet_jobs_adf import implnet_job_adf
from sch.implnet_sch_adf  import implnet_sch_adf
from jobs.implnet_jobs_asulrdr import implnet_job_asulrdr
from sch.implnet_sch_asulrdr  import implnet_sch_asulrdr
from jobs.implnet_jobs_aussda import implnet_job_aussda
from sch.implnet_sch_aussda  import implnet_sch_aussda
from jobs.implnet_jobs_borealis import implnet_job_borealis
from sch.implnet_sch_borealis  import implnet_sch_borealis
from jobs.implnet_jobs_cifor import implnet_job_cifor
from sch.implnet_sch_cifor  import implnet_sch_cifor
from jobs.implnet_jobs_cimmyt import implnet_job_cimmyt
from sch.implnet_sch_cimmyt  import implnet_sch_cimmyt
from jobs.implnet_jobs_cora import implnet_job_cora
from sch.implnet_sch_cora  import implnet_sch_cora
from jobs.implnet_jobs_crossda import implnet_job_crossda
from sch.implnet_sch_crossda  import implnet_sch_crossda
from jobs.implnet_jobs_cuhk import implnet_job_cuhk
from sch.implnet_sch_cuhk  import implnet_sch_cuhk
from jobs.implnet_jobs_tdi import implnet_job_tdi
from sch.implnet_sch_tdi  import implnet_sch_tdi
from jobs.implnet_jobs_darus import implnet_job_darus
from sch.implnet_sch_darus  import implnet_sch_darus
from jobs.implnet_jobs_irs import implnet_job_irs
from sch.implnet_sch_irs  import implnet_sch_irs
from jobs.implnet_jobs_sceincespo import implnet_job_sceincespo
from sch.implnet_sch_sceincespo  import implnet_sch_sceincespo
from jobs.implnet_jobs_edatos import implnet_job_edatos
from sch.implnet_sch_edatos  import implnet_sch_edatos
from jobs.implnet_jobs_netherland import implnet_job_netherland
from sch.implnet_sch_netherland  import implnet_sch_netherland
from jobs.implnet_jobs_norway import implnet_job_norway
from sch.implnet_sch_norway  import implnet_sch_norway
from jobs.implnet_jobs_ntu import implnet_job_ntu
from sch.implnet_sch_ntu  import implnet_sch_ntu
from jobs.implnet_jobs_fiu import implnet_job_fiu
from sch.implnet_sch_fiu  import implnet_sch_fiu
from jobs.implnet_jobs_gro import implnet_job_gro
from sch.implnet_sch_gro  import implnet_sch_gro
from jobs.implnet_jobs_harvard import implnet_job_harvard
from sch.implnet_sch_harvard  import implnet_sch_harvard
from jobs.implnet_jobs_hord import implnet_job_hord
from sch.implnet_sch_hord  import implnet_sch_hord
from jobs.implnet_jobs_ibict import implnet_job_ibict
from sch.implnet_sch_ibict  import implnet_sch_ibict
from jobs.implnet_jobs_icrisat import implnet_job_icrisat
from sch.implnet_sch_icrisat  import implnet_sch_icrisat
from jobs.implnet_jobs_ifdc import implnet_job_ifdc
from sch.implnet_sch_ifdc  import implnet_sch_ifdc
from jobs.implnet_jobs_ifsttar import implnet_job_ifsttar
from sch.implnet_sch_ifsttar  import implnet_sch_ifsttar
from jobs.implnet_jobs_iisg import implnet_job_iisg
from sch.implnet_sch_iisg  import implnet_sch_iisg
from jobs.implnet_jobs_irl import implnet_job_irl
from sch.implnet_sch_irl  import implnet_sch_irl
from jobs.implnet_jobs_ipc import implnet_job_ipc
from sch.implnet_sch_ipc  import implnet_sch_ipc
from jobs.implnet_jobs_iit import implnet_job_iit
from sch.implnet_sch_iit  import implnet_sch_iit
from jobs.implnet_jobs_hopkins import implnet_job_hopkins
from sch.implnet_sch_hopkins  import implnet_sch_hopkins
from jobs.implnet_jobs_julich import implnet_job_julich
from sch.implnet_sch_julich  import implnet_sch_julich
from jobs.implnet_jobs_uva import implnet_job_uva
from sch.implnet_sch_uva  import implnet_sch_uva
from jobs.implnet_jobs_rin import implnet_job_rin
from sch.implnet_sch_rin  import implnet_sch_rin
from jobs.implnet_jobs_lida import implnet_job_lida
from sch.implnet_sch_lida  import implnet_sch_lida
from jobs.implnet_jobs_icarda import implnet_job_icarda
from sch.implnet_sch_icarda  import implnet_sch_icarda
from jobs.implnet_jobs_nioz import implnet_job_nioz
from sch.implnet_sch_nioz  import implnet_sch_nioz
from jobs.implnet_jobs_ucdl import implnet_job_ucdl
from sch.implnet_sch_ucdl  import implnet_sch_ucdl
from jobs.implnet_jobs_ofd import implnet_job_ofd
from sch.implnet_sch_ofd  import implnet_sch_ofd
from jobs.implnet_jobs_peking import implnet_job_peking
from sch.implnet_sch_peking  import implnet_sch_peking
from jobs.implnet_jobs_pucdp import implnet_job_pucdp
from sch.implnet_sch_pucdp  import implnet_sch_pucdp
from jobs.implnet_jobs_qdr import implnet_job_qdr
from sch.implnet_sch_qdr  import implnet_sch_qdr
from jobs.implnet_jobs_chile import implnet_job_chile
from sch.implnet_sch_chile  import implnet_sch_chile
from jobs.implnet_jobs_rosario import implnet_job_rosario
from sch.implnet_sch_rosario  import implnet_sch_rosario
from jobs.implnet_jobs_pesquisa import implnet_job_pesquisa
from sch.implnet_sch_pesquisa  import implnet_sch_pesquisa
from jobs.implnet_jobs_rsu import implnet_job_rsu
from sch.implnet_sch_rsu  import implnet_sch_rsu
from jobs.implnet_jobs_tdl import implnet_job_tdl
from sch.implnet_sch_tdl  import implnet_sch_tdl
from jobs.implnet_jobs_ucla import implnet_job_ucla
from sch.implnet_sch_ucla  import implnet_sch_ucla
from jobs.implnet_jobs_unb import implnet_job_unb
from sch.implnet_sch_unb  import implnet_sch_unb
from jobs.implnet_jobs_unc import implnet_job_unc
from sch.implnet_sch_unc  import implnet_sch_unc
from jobs.implnet_jobs_manitoba import implnet_job_manitoba
from sch.implnet_sch_manitoba  import implnet_sch_manitoba
from jobs.implnet_jobs_milano import implnet_job_milano
from sch.implnet_sch_milano  import implnet_sch_milano
from jobs.implnet_jobs_uwi import implnet_job_uwi
from sch.implnet_sch_uwi  import implnet_sch_uwi
from jobs.implnet_jobs_vtti import implnet_job_vtti
from sch.implnet_sch_vtti  import implnet_sch_vtti
from jobs.implnet_jobs_wardr import implnet_job_wardr
from sch.implnet_sch_wardr  import implnet_sch_wardr
from jobs.implnet_jobs_yalenus import implnet_job_yalenus
from sch.implnet_sch_yalenus  import implnet_sch_yalenus
 
@repository
def gleaner():
	jobs = [implnet_job_arecibo, implnet_job_aws, implnet_job_cyvers, implnet_job_drp, implnet_job_dryad, implnet_job_matcommons, implnet_job_mdf, implnet_job_neon, implnet_job_abacus, implnet_job_acss, implnet_job_adf, implnet_job_asulrdr, implnet_job_aussda, implnet_job_borealis, implnet_job_cifor, implnet_job_cimmyt, implnet_job_cora, implnet_job_crossda, implnet_job_cuhk, implnet_job_tdi, implnet_job_darus, implnet_job_irs, implnet_job_sceincespo, implnet_job_edatos, implnet_job_netherland, implnet_job_norway, implnet_job_ntu, implnet_job_fiu, implnet_job_gro, implnet_job_harvard, implnet_job_hord, implnet_job_ibict, implnet_job_icrisat, implnet_job_ifdc, implnet_job_ifsttar, implnet_job_iisg, implnet_job_irl, implnet_job_ipc, implnet_job_iit, implnet_job_hopkins, implnet_job_julich, implnet_job_uva, implnet_job_rin, implnet_job_lida, implnet_job_icarda, implnet_job_nioz, implnet_job_ucdl, implnet_job_ofd, implnet_job_peking, implnet_job_pucdp, implnet_job_qdr, implnet_job_chile, implnet_job_rosario, implnet_job_pesquisa, implnet_job_rsu, implnet_job_tdl, implnet_job_ucla, implnet_job_unb, implnet_job_unc, implnet_job_manitoba, implnet_job_milano, implnet_job_uwi, implnet_job_vtti, implnet_job_wardr, implnet_job_yalenus]
	schedules = [implnet_sch_arecibo, implnet_sch_aws, implnet_sch_cyvers, implnet_sch_drp, implnet_sch_dryad, implnet_sch_matcommons, implnet_sch_mdf, implnet_sch_neon, implnet_sch_abacus, implnet_sch_acss, implnet_sch_adf, implnet_sch_asulrdr, implnet_sch_aussda, implnet_sch_borealis, implnet_sch_cifor, implnet_sch_cimmyt, implnet_sch_cora, implnet_sch_crossda, implnet_sch_cuhk, implnet_sch_tdi, implnet_sch_darus, implnet_sch_irs, implnet_sch_sceincespo, implnet_sch_edatos, implnet_sch_netherland, implnet_sch_norway, implnet_sch_ntu, implnet_sch_fiu, implnet_sch_gro, implnet_sch_harvard, implnet_sch_hord, implnet_sch_ibict, implnet_sch_icrisat, implnet_sch_ifdc, implnet_sch_ifsttar, implnet_sch_iisg, implnet_sch_irl, implnet_sch_ipc, implnet_sch_iit, implnet_sch_hopkins, implnet_sch_julich, implnet_sch_uva, implnet_sch_rin, implnet_sch_lida, implnet_sch_icarda, implnet_sch_nioz, implnet_sch_ucdl, implnet_sch_ofd, implnet_sch_peking, implnet_sch_pucdp, implnet_sch_qdr, implnet_sch_chile, implnet_sch_rosario, implnet_sch_pesquisa, implnet_sch_rsu, implnet_sch_tdl, implnet_sch_ucla, implnet_sch_unb, implnet_sch_unc, implnet_sch_manitoba, implnet_sch_milano, implnet_sch_uwi, implnet_sch_vtti, implnet_sch_wardr, implnet_sch_yalenus]

 
	return jobs + schedules
