class RitualManager:
    def __init__(self):
        self.rituals = []

    def perform_ritual(self, name, steps, emotion):
        self.rituals.append({ "name": name, "steps": steps, "emotion": emotion })
        return f"Ritual '{name}' performed with {emotion}."