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
print(BUILD_DIR)

@app.command()
def create():
    print("Creating user: Hiro Hamada")


@app.command()
def gleaner(sitemap: Annotated[str, typer.Option()] = "https://geoconnex.us/sitemap.xml",
            base: Annotated[str, typer.Option()] = "gleanerconfigPREFIX.example.yaml"
            ):

    def remove_non_alphanumeric(string):
        return re.sub(r'[^a-zA-Z0-9]+', '', string)

    # parse the sitemap INDEX for the referenced sitemaps for a config file
    Lines = []

    r = requests.get(sitemap)
    xml = r.text
    soup = BeautifulSoup(xml, features='xml')
    sitemapTags = soup.find_all("sitemap")

    for sitemap in sitemapTags:
        Lines.append(sitemap.findNext("loc").text) # type: ignore


    sources = []
    for line in Lines:
        data = {}

        target = line.rsplit('/', 1)[-1]
        name =  remove_non_alphanumeric(target.lower().replace(".xml", ""))
        data["sourcetype"] = "sitemap"
        data["name"] = str("{}".format(name))
        data["url"] = line.strip()
        data["headless"] = "false"
        data["pid"] = "https://gleaner.io/genid/geoconnex"
        data["propername"] = str("{}".format(name))
        data["domain"] = "https://geoconnex.us"
        data["active"] = "true"
        sources.append(data)

    with open(os.path.join(BUILD_DIR, 'gleanerconfig.yaml'), 'w') as outfile:
        yaml.dump(sources, outfile, default_flow_style=False)


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