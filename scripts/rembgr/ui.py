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

        return [
            rb_enabled
        ]
