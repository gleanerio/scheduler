import setuptools

setuptools.setup(
    name="gleaner",
    packages=setuptools.find_packages(exclude=["gleaner_tests"]),
    install_requires=[
        "dagster==0.15.3",
        "dagit==0.15.3",
        "pytest",
    ],
)
