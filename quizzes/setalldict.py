# -------------------------
# title: SetAllDict
# -------------------------
# -------------------------
# Description:
# Make set_all in O(1).
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: 
# AI2 InfinityLabs.
# ----------------------------
class SetAllDict:
    def __init__(self):
        self.d = {}
        self.global_value = None
        self.global_version = -1
        self.current_version = 0

    def __setitem__(self, key, value):
        self.d[key] = (value, self.current_version)

    def __getitem__(self, key):
        if key not in self.d:
            raise KeyError(f"Key '{key}' not found.")
        value, version = self.d[key]
        return self.global_value if version < self.global_version else value

    def __str__(self):
        return str({key: self[key] for key in self.d})

    def set_all(self, value):
        self.global_value = value
        self.global_version += 1