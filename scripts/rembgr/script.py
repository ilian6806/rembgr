import gc

import modules.shared as shared
from modules import images, devices
from . import bgr_remover


class RemoveBackgroundCore():

    def execute_postprocess(self, p, processed,
        rb_enabled,
        rb_add_background_color,
        rb_background_color,
        rb_bgr_image_enabled,
        rb_bgr_image,
        rb_fgr_image
    ):

        if not rb_enabled:
            return

        new_images = []

        def save_image(image):
            new_images.append(image)
            images.save_image(
                image,
                p.outpath_samples,
                "",
                p.seed,
                p.prompt,
                shared.opts.samples_format,
                info=processed.info,
                p=p
            )

        for image in processed.images:

            devices.torch_gc()
            gc.collect()

            new_image = bgr_remover.process(image)
            save_image(new_image)

            if rb_add_background_color:
                new_image_with_background = bgr_remover.add_background(new_image, rb_background_color)
                save_image(new_image_with_background)

            if rb_bgr_image_enabled:
                to_merge = []
                if rb_bgr_image:
                    to_merge.append(rb_bgr_image)
                to_merge.append(new_image)
                if rb_fgr_image:
                    to_merge.append(rb_fgr_image)
                merged = bgr_remover.merge_images(to_merge)
                save_image(merged)

        processed.images = processed.images + new_images

        devices.torch_gc()
        gc.collect()
