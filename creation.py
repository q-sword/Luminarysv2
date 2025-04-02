class ArchiveOfInvention:
    def __init__(self):
        self.idea_seeds = []

    def plant_seed(self, title, description):
        self.idea_seeds.append({ "title": title, "description": description })
        return f"Seed '{title}' planted."