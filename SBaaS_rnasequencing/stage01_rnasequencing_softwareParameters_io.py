# System
import json
import copy
# SBaaS
from .stage01_rnasequencing_softwareParameters_query import stage01_rnasequencing_softwareParameters_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage01_rnasequencing_softwareParameters_io(stage01_rnasequencing_softwareParameters_query,
                                    sbaas_template_io #abstract io methods
                                    ):
    pass;