'''
API for Rembgr - Stable Diffusion Web UI extension.
Core logic is in rembgr.api.

Author: ilian.iliev
Since: 09.01.2023
'''

import os
import sys

from modules import scripts
sys.path.append(os.path.join(scripts.basedir(), 'scripts'))

import modules.script_callbacks as script_callbacks
from rembgr.api import RembgrApi

try:
    api = RembgrApi()
    script_callbacks.on_app_started(api.start)
except:
    pass
