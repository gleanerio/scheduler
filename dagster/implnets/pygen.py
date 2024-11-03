import yaml
import argparse
# from typing import Tuple
import tempfile
import os
import fileinput
import re
import shutil
import pydash

#  python pygen.py -cf ../../configs/oih/gleanerconfig.yaml -od ./output -td ./templates

def gencode(cf, od, td, days) -> str:
    # read config
    c = yaml.safe_load(open(cf, 'r'))

    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)
        operations = ["ops", "jobs", "sch"]

        # Get the count and divide into the hour count range (time
        # interval) we want to sprad thm over.
        hours = int(days) * 24  # days is the cli param for the number of days to work over
        inc = round(hours / len(c["sources"])) # divide hours we want to run over by number of source to get increment

        print("index event every {} hours over {} day(s) period for {} items".format(inc, days, len(c["sources"])))
        sources = pydash.union_by(c["sources"], lambda source: source["name"])
        #for i, s in enumerate(c["sources"]):
        for i, s in enumerate(sources):

            # could put an if statement here for those that are active
            # print(s["name"])

            # copy the templates to the temp dir
            for operation in operations:
                src = "{0}/implnet_{1}_SOURCEVAL.py".format(td, operation)
                dst = "{0}/implnet_{1}_{2}.py".format(tmpdirname, operation, s["name"])
                shutil.copyfile(src, dst)

                # update the templates loop 1
                with open(dst, 'r') as file:
                    file_contents = file.read()

                # replace the desired text in the string
                new_contents = file_contents.replace("SOURCEVAL", s["name"])

                # write the new contents back to the file
                with open(dst, 'w') as file:
                    file.write(new_contents)

                # update the templates loop 2
                if "sch" in operation:
                    di = int(days)
                    q = (((i * inc) / 24) % di) // 1
                    r = (i * inc) % 24
                    new_cron_schedule = "0 {} {} * *".format(r, int(q)+1)
                    pattern = r'cron_schedule="(.+?)"'
                    # print("index {}::  {}".format(i,new_cron_schedule))
                    for line in fileinput.input(dst, inplace=True):
                        line = re.sub(pattern, f'cron_schedule="{new_cron_schedule}"', line)
                        # line = re.sub(r'0 24 * * *', f'0 {r} * * {int(q)}', line)
                        print(line, end='')

                        # make directories in the output directory
            for operation in operations:
                if not os.path.exists("{0}/{1}".format(od, operation)):
                    os.makedirs("{0}/{1}".format(od, operation))

            # copy new files to output dir
            for operation in operations:
                src = "{0}/implnet_{1}_{2}.py".format(tmpdirname, operation, s["name"])
                dst = "{0}/{1}/implnet_{1}_{2}.py".format(od, operation, s["name"])
                shutil.copyfile(src, dst)

    return "done"


def repo(cf, od) -> str:
    repofile = "{0}/repositories/repository.py".format(od)

    if not os.path.exists("{0}/repositories".format(od)):
        os.makedirs("{0}/repositories".format(od))

    c = yaml.safe_load(open(cf, 'r'))

    with open(repofile, 'w+') as file:
        file.write("from dagster import repository\n")

        for s in c["sources"]:
            file.write("from jobs.implnet_jobs_{0} import implnet_job_{0}\n".format(s["name"]))
            file.write("from sch.implnet_sch_{0}  import implnet_sch_{0}\n".format(s["name"]))

        file.write(" \n")

        file.write("@repository\n")
        file.write("def gleaner():\n")

        ja = []
        sa = []
        for s in c["sources"]:
            ja.append("implnet_job_{}".format(s["name"]))
            sa.append("implnet_sch_{}".format(s["name"]))

        ja_str = ", ".join(ja)
        sa_str = ", ".join(sa)
        file.write("\tjobs = [{}]\n".format(ja_str))
        file.write("\tschedules = [{}]\n\n".format(sa_str))

        file.write(" \n")

        file.write("\treturn jobs + schedules\n")

    return "done"


def workspace(od) -> str:
    workspacefile = "{0}/workspace.yaml".format(od)

    with open(workspacefile, 'w') as file:
        file.write("""load_from:
      - python_file:
          relative_path: "repositories/repository.py"
          working_directory: .""")

    return "done"


def main():
    # Initialize args  parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-cf", "--config", help="Gleaner config to use as source")
    parser.add_argument("-od", "--outputs", help="Directory for output")
    parser.add_argument("-td", "--templates", help="Directory where the template files are")
    parser.add_argument("-d", "--days", help="Days to spread the run over")
    parser.add_argument("-w", "--weekly", help="Spread the run over a week")
    parser.add_argument("-m", "--monthly", help="Spread the run over a month")
    args = parser.parse_args()

    cf = args.config
    od = args.outputs
    td = args.templates
    days = args.days

    s1 = gencode(cf, od, td, days)
    s2 = repo(cf, od)
    s3 = workspace(od)

    print("{}  {}  {}".format(s1, s2, s3))


if __name__ == '__main__':
    main()
