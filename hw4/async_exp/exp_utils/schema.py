class ModelResponse:
    def __init__(self, model, inference_parameters, inference_time, num_token, raw_output):
        self.model = model
        self.inference_parameters = inference_parameters
        self.inference_time = inference_time
        self.num_token = num_token
        self.raw_output = raw_output
    
    def model_dump(self):
        return {
            'model': self.model,
            'inference_parameters': self.inference_parameters,
            'inference_time': self.inference_time,
            'num_token': self.num_token,
            'raw_output': self.raw_output
        }
