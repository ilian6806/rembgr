import gradio as gr

from . import constants


class RemoveBackgroundUI():

    def __init__(self, rb_script):
        self.rb_script = rb_script
        self.rb_core = rb_script.rb_core

    def get_elem_id_prefix(self):
        return 'rb-'

    def get_id(self, id, is_img2img):
        return "%s%s-%s" % (self.get_elem_id_prefix(), id, "img2img" if is_img2img else "txt2img")

    def render(self, is_img2img):
        with gr.Group():
            with gr.Accordion(constants.script_name, open=False):
                with gr.Group(elem_id=self.get_id("container", is_img2img)):
                    result = self.render_inner(is_img2img)
        return result

    def render_inner(self, is_img2img):

        def get_id(id):
            return self.get_id(id, is_img2img)

        with gr.Row():
            rb_enabled = gr.Checkbox(elem_id=get_id("enabled"), label="Enable", value=False, visible=True)
        with gr.Row():
            with gr.Column(scale=1):
                rb_add_background_color = gr.Checkbox(elem_id=get_id("use-background-color"), label="Add background color", value=False)
            with gr.Column(scale=2):
                rb_background_color = gr.ColorPicker(
                    elem_id=get_id("background-color"),
                    show_label=False,
                    interactive=True
                )
        with gr.Row():
            rb_bgr_image_enabled = gr.Checkbox(elem_id=get_id("bgr_image_enabled"), label="Add background image", value=False, visible=True)
        with gr.Row(visible=False) as images_row:
            rb_bgr_image = gr.Image(
                elem_id="bgr_image",
                label="Background",
                source="upload",
                interactive=True,
                type="pil",
                tool="editor",
                image_mode="RGBA"
            )

            rb_fgr_image = gr.Image(
                elem_id="fgr_image",
                label="Foreground",
                source="upload",
                interactive=True,
                type="pil",
                tool="editor",
                image_mode="RGBA"
            )

            rb_bgr_image_enabled.change(
                lambda visible: {"visible": visible, "__type__": "update"},
                inputs=[rb_bgr_image_enabled],
                outputs=[images_row]
            )

        return [
            rb_enabled,
            rb_add_background_color,
            rb_background_color,
            rb_bgr_image_enabled,
            rb_bgr_image,
            rb_fgr_image
        ]
