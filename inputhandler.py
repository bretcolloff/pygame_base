

class InputHandler:
    def __init__(self):
        self.focus = None

    def set_focus(self, focus):
        self.focus = focus

    def apply_input(self, input_map):
        self.focus.process_input(input_map)
