# Dagster notes

* run the indexes every 3 days at first, then every week
(could have sensor triggers too)
* index each source spaced by two hours
* do a graph load after each indexing
* do a SHACL eval after each indexing



## OIH sources

      name: aquadocs
      name: edmerp
      name: edmo
      name: euroceanevents
      name: euroceanexpert
      name: euroceanorgs
      name: euroceanprojects
      name: euroceantraining
      name: euroceanvessels
      name: invemardocuments
      name: invemarexpert
      name: invemarinstitution
      name: invemartraining
      name: invemarvessel
      name: marinetraining
      name: obis
      name: obps
      name: oceanexperts

## OIH Queue (sources being worked on)

    name: cioosatlantic
    name: inanodc
    name: maspawio
    name: benguelacc
    name: caribbeanmarineatlas
    name: emodnet
    name: pogo
    name: pdh




oih_job_aquadocs, oih_job_edmerp, oih_job_edmo, oih_job_euroceanevents, oih_job_euroceanexpert, oih_job_euroceanorgs, oih_job_euroceanprojects, oih_job_euroceantraining, oih_job_euroceanvessels, oih_job_invemardocuments, oih_job_invemarexpert, oih_job_invemarinstitution, oih_job_invemartraining, oih_job_invemarvessel, oih_job_marinetraining, oih_job_obis, oih_job_obps, oih_job_oceanexperts



oih_sch_aquadocs, oih_sch_edmerp, oih_sch_edmo, oih_sch_euroceanevents, oih_sch_euroceanexpert, oih_sch_euroceanorgs, oih_sch_euroceanprojects, oih_sch_euroceantraining, oih_sch_euroceanvessels, oih_sch_invemardocuments, oih_sch_invemarexpert, oih_sch_invemarinstitution, oih_sch_invemartraining, oih_sch_invemarvessel, oih_sch_marinetraining, oih_sch_obis, oih_sch_obps, oih_sch_oceanexperts



10063  for NAME in edmo euroceanevents euroceanexpert euroceanorgs euroceanprojects euroceantraining euroceanvessels invemardocuments invemarexpert invemarinstitution invemartraining invemarvessel marinetraining obis obps oceanexperts; cp oih_edmerp.py oih_$NAME.py; done
10065  for NAME in edmo euroceanevents euroceanexpert euroceanorgs euroceanprojects euroceantraining euroceanvessels invemardocuments invemarexpert invemarinstitution invemartraining invemarvessel marinetraining obis obps oceanexperts; do cp oih_edmerp.py oih_$NAME.py; done
10068  for NAME in edmo euroceanevents euroceanexpert euroceanorgs euroceanprojects euroceantraining euroceanvessels invemardocuments invemarexpert invemarinstitution invemartraining invemarvessel marinetraining obis obps oceanexperts; do sed -i 's/edmerp/$NAME/g' oih_$NAME.py ; done
10069  for NAME in edmo euroceanevents euroceanexpert euroceanorgs euroceanprojects euroceantraining euroceanvessels invemardocuments invemarexpert invemarinstitution invemartraining invemarvessel marinetraining obis obps oceanexperts; do rm  oih_$NAME.py ; done
10070  for NAME in edmo euroceanevents euroceanexpert euroceanorgs euroceanprojects euroceantraining euroceanvessels invemardocuments invemarexpert invemarinstitution invemartraining invemarvessel marinetraining obis obps oceanexperts; do cp oih_edmerp.py oih_$NAME.py; done
10071  for NAME in edmo euroceanevents euroceanexpert euroceanorgs euroceanprojects euroceantraining euroceanvessels invemardocuments invemarexpert invemarinstitution invemartraining invemarvessel marinetraining obis obps oceanexperts; do sed -i "s/edmerp/$NAME/g" oih_$NAME.py ; done
10072  for NAME in edmo euroceanevents euroceanexpert euroceanorgs euroceanprojects euroceantraining euroceanvessels invemardocuments invemarexpert invemarinstitution invemartraining invemarvessel marinetraining obis obps oceanexperts; do sed -i "s/oih_queue/oih_local/g" oih_$NAME.py ; done
10074  for NAME in edmerp edmo euroceanevents euroceanexpert euroceanorgs euroceanprojects euroceantraining euroceanvessels invemardocuments invemarexpert invemarinstitution invemartraining invemarvessel marinetraining obis obps oceanexperts; do cp oih_jobs_aquadocs.py oih_jobs_$NAME.py; done
10075  for NAME in edmo euroceanevents euroceanexpert euroceanorgs euroceanprojects euroceantraining euroceanvessels invemardocuments invemarexpert invemarinstitution invemartraining invemarvessel marinetraining obis obps oceanexperts; do sed -i "s/aquadocs/$NAME/g" oih_job_$NAME.py ; done
10076  for NAME in edmo euroceanevents euroceanexpert euroceanorgs euroceanprojects euroceantraining euroceanvessels invemardocuments invemarexpert invemarinstitution invemartraining invemarvessel marinetraining obis obps oceanexperts; do sed -i "s/aquadocs/$NAME/g" oih_jobs_$NAME.py ; done
