'''
Remove Background - Stable Diffusion Web UI extension for removing background from images
Core logic is in rembgr.script.

Author: ilian.iliev
Since: 09.03.2023
'''

import os
import sys

from modules import scripts
sys.path.append(os.path.join(scripts.basedir(), 'scripts'))

from rembgr import script, ui, constants


class RemoveBackgroundScript(scripts.Script):

    def __init__(self, *k, **kw):
        self.rb_core = script.RemoveBackgroundCore()
        self.rb_ui = ui.RemoveBackgroundUI(self)
        super().__init__()

    def title(self):
        return constants.script_name

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        return self.rb_ui.render(is_img2img)

    def postprocess(self, p, processed, *args):
        return self.rb_core.execute_postprocess(p, processed, *args)
