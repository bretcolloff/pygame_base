
""" Handles input and applies it. """
class InputHandler:
    def __init__(self):
        self.focus = None

    # Set the entity that will use the provided input.
    def set_focus(self, focus):
        self.focus = focus

    # Applies input to the focussed element.
    def apply_input(self, input_map):
        self.focus.process_input(input_map)
