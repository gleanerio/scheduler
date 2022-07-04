import setuptools

setuptools.setup(
    name="oih",
    packages=setuptools.find_packages(exclude=["oih_tests"]),
    install_requires=[
        "dagster==0.14.7",
        "dagit==0.14.7",
        "pytest",
    ],
)
