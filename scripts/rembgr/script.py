import gc

import modules.shared as shared
from modules import images
from . import bgr_remover


class RemoveBackgroundCore():

    def execute_postprocess(self, p, processed, rb_enabled):

        if not rb_enabled:
            return

        new_images = []

        for image in processed.images:

            new_image = bgr_remover.process(image)
            new_images.append(new_image)

            images.save_image(
                new_image,
                p.outpath_samples,
                "",
                p.seed,
                p.prompt,
                shared.opts.samples_format,
                info=processed.info,
                p=p
            )

        processed.images = processed.images + new_images
        gc.collect()
