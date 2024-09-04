import fileinput
import os
import re
import tempfile
from typing import Annotated
from bs4 import BeautifulSoup
import requests
import typer
import shutil

import yaml

app = typer.Typer()

BUILD_DIR =  os.path.join(os.path.dirname(__file__), "build")
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")

def gencode(cf, od, td, days) -> str:
    """Generate code"""
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

        for i, s in enumerate(c["sources"]):

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

@app.command()
def generate_jobs(
    # weekly: Annotated[int, typer.Option(help="Spread the run over a week")],
    # monthly: Annotated[str, typer.Option(help="Spread the run over a month")],
    config: Annotated[str, typer.Option(help="Gleaner config to use as source")] = os.path.join(BUILD_DIR, "gleanerconfig.yaml"),
    outputs: Annotated[str, typer.Option(help="Directory for output")] = BUILD_DIR,
    templates: Annotated[str, typer.Option(help="Directory where the template files are")] = TEMPLATE_DIR,
    days: Annotated[int, typer.Option(help="Days to spread the run over")] = 27

):
    """Generate the Python files for each dagster job"""
    
    gencode(config, outputs, templates, days)
    repo(config, outputs)
    

    with open(os.path.join(BUILD_DIR, "workspace.yaml"), 'w') as file:
        file.write("""load_from:
      - python_file:
          relative_path: "repositories/repository.py"
          working_directory: .""")




@app.command()
def generate_config(sitemap: Annotated[str, typer.Option()] = "https://geoconnex.us/sitemap.xml",
            base: Annotated[str, typer.Option()] = "gleanerconfigPREFIX.example.yaml"
            ):
    """Generate the gleaner config from a remote sitemap"""

    def remove_non_alphanumeric(string):
        return re.sub(r'[^a-zA-Z0-9]+', '', string)

    # Load the base YAML file
    with open(base, 'r') as base_file:
        base_data = yaml.safe_load(base_file)

    # Parse the sitemap INDEX for the referenced sitemaps for a config file
    Lines = []

    r = requests.get(sitemap)
    xml = r.text
    soup = BeautifulSoup(xml, features='xml')
    sitemapTags = soup.find_all("sitemap")

    for sitemap in sitemapTags:
        Lines.append(sitemap.findNext("loc").text)  # type: ignore

    sources = []
    for line in Lines:
        data = {}

        target = line.rsplit('/', 1)[-1]
        name = remove_non_alphanumeric(target.lower().replace(".xml", ""))
        data["sourcetype"] = "sitemap"
        data["name"] = name
        data["url"] = line.strip()
        data["headless"] = "false"
        data["pid"] = "https://gleaner.io/genid/geoconnex"
        data["propername"] = name
        data["domain"] = "https://geoconnex.us"
        data["active"] = "true"
        sources.append(data)

    # Combine base data with the new sources
    if isinstance(base_data, dict):
        base_data["sources"] = sources
    else:
        base_data = {"sources": sources}

    # Write the combined data to the output YAML file
    with open(os.path.join(BUILD_DIR, 'gleanerconfig.yaml'), 'w') as outfile:
        yaml.dump(base_data, outfile, default_flow_style=False)


@app.command()
def clean():
    """Delete the contents of the build directory"""

    if os.path.exists(BUILD_DIR):
        print("Cleaning contents of the build directory")
        
        for root, dirs, files in os.walk(BUILD_DIR):
            for name in files:
                if name != '.gitkeep':
                    os.remove(os.path.join(root, name))
            for name in dirs:
                shutil.rmtree(os.path.join(root, name))
    else:
        print("Build directory does not exist")

if __name__ == "__main__":
    app()