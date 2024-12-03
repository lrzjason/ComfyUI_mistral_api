from .pixtral_node import ComfyUIPixtral, MultiImagesInput, preview_text

NODE_CLASS_MAPPINGS = {
    "ComfyUIPixtral": ComfyUIPixtral,
    "MultiImagesInput": MultiImagesInput,
    "preview_text": preview_text,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUIPixtral": "Pixtral",
    "MultiImagesInput": "Multi Images Input",
    "preview_text": "Preview Text",
}

WEB_DIRECTORY = "web"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']