"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from .params import PARAMS
from seatable_api import Base

log = getLogger("module")

base = Base(PARAMS['API_TOKEN'], 'https://cloud.seatable.io')
base.auth()

def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Writing to SeaTable ...")

    try:
        if type(received_data) is list:
            base.batch_append_rows(PARAMS['TABLE'], received_data)
        else:
            base.append_row(PARAMS['TABLE'], received_data)

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"
