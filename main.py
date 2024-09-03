import os
import re
from typing import Annotated
from bs4 import BeautifulSoup
import requests
import typer
import shutil

import yaml

app = typer.Typer()

BUILD_DIR =  os.path.join(os.path.dirname(__file__), "build")

@app.command()
def generate_jobs(
    outputs: Annotated[str, typer.Option(help="Directory for output")],
    templates: Annotated[str, typer.Option(help="Directory where the template files are")],
    days: Annotated[str, typer.Option(help="Days to spread the run over")],
    weekly: Annotated[str, typer.Option(help="Spread the run over a week")],
    monthly: Annotated[str, typer.Option(help="Spread the run over a month")],
    config: Annotated[str, typer.Option(help="Gleaner config to use as source")] = os.path.join(BUILD_DIR, "gleanerconfig.yaml"),

):
    """Generate the """
    pass  # Replace with your function implementation



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