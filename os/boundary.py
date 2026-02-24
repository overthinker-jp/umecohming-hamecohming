# OS Boundary Prototype

class OSBoundary:

    def __init__(self, hame_rules):
        self.hame_rules = hame_rules

    def match(self, ume_attributes):
        return all(rule in ume_attributes for rule in self.hame_rules)

    def verify(self, ume_attributes):
        result = "MATCH_OK" if self.match(ume_attributes) else "STRUCTURAL_SILENCE"
        log = {
            "hame_rules": self.hame_rules,
            "ume_attributes": ume_attributes,
            "result": result
        }
        return result, log
