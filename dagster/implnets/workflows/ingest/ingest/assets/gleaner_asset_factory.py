
from dagster import get_dagster_logger, asset, In, Nothing, Config

from ..resources import gleanerio
class gleaner(Config):
   source: str

   def create_gleaner_asset(self,context):
        @asset(name=f"{self.source}_gleaner")
        def _gleanerio():
            gleanerio(context, ("gleaner"), self.source)

        return _gleanerio()
