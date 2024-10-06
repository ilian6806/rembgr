from fastapi import FastAPI, Body, HTTPException, Request, Response
from fastapi.responses import FileResponse

import gradio as gr
import modules.shared as shared
import modules.script_callbacks as script_callbacks

from .models import SingleImageRequest, SingleImageResponse
from .utils import encode_pil_to_base64, decode_base64_to_image
from ..bgr_remover import process


class RembgrApi():

    BASE_PATH = '/sdapi/v1/rembg'

    def get_path(self, path):
        return f"{self.BASE_PATH}{path}"

    def add_api_route(self, path: str, endpoint, **kwargs):
        return self.app.add_api_route(self.get_path(path), endpoint, **kwargs)

    def start(self, _: gr.Blocks, app: FastAPI):
        self.app = app
        self.add_api_route('/process', self.process, methods=['POST'])

    def process(self, req: SingleImageRequest):
        """Process an image and return it without background."""
        image = decode_base64_to_image(req.image)
        result = process(image)
        return SingleImageResponse(image=encode_pil_to_base64(result))
