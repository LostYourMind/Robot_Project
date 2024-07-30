import base64
from inference_sdk import InferenceHTTPClient

class RoboflowClient:
    def __init__(self, api_url, api_key):
        self.client = InferenceHTTPClient(api_url=api_url, api_key=api_key)
    
    def infer_image(self, image_path, model_id):
        with open(image_path, 'rb') as f:
            image_data = f.read()
            encoded_image = base64.b64encode(image_data).decode('utf-8')
        
        result = self.client.infer(encoded_image, model_id=model_id)
        return result

    def get_class_from_result(self, result):
        return result['predictions'][0]['class'] if result['predictions'] else None
