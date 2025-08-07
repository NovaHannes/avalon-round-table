class AgentInterface:
    def __init__(self, name):
        self.name = name

    def deliberate(self, prompt):
        return f"Simulated response from {self.name} to prompt: '{prompt}'"
