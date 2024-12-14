class ModelResponse:
    def __init__(self, model, inference_parameters, inference_time, num_token, raw_output):
        self.model = model
        self.inference_parameters = inference_parameters
        self.inference_time = inference_time
        self.num_token = num_token
        self.raw_output = raw_output
