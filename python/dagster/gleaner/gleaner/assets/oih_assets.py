from dagster import asset

@asset
def oih_asset():
        return ["euroceanevents"]

@asset
def asset_ee(oih_asset):
        return oih_asset[0]


