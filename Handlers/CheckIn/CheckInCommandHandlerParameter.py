from Handlers.BaseCommandHandlerParameter import BaseCommandHandlerParameter

class CheckInCommandHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self,image, operation_type):
        self.image = image
        self.operation_type = operation_type