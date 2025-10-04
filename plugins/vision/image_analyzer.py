from PIL import Image
import io

class ImageAnalyzerPlugin:
    name = "image_analyzer"
    description = "Analyze images. Usage: use_plugin('image_analyzer', image_bytes=<bytes>)"

    def run(self, image_bytes):
        try:
            image = Image.open(io.BytesIO(image_bytes))
            return f"Image format: {image.format}, size: {image.size}, mode: {image.mode}"
        except Exception as e:
            return f"Image analysis error: {e}"
