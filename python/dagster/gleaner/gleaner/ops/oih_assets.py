from dagster import AssetMaterialization, op

@op
def oih_assetmat(context):
        df = read_df()
        remote_storage_path = persist_to_storage(df)
        context.log_event(
            AssetMaterialization(
                 asset_key="ee_key", description="euroceanevent"
            )
        )

return remote_storage_path

