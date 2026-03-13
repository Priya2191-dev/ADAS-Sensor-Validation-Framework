class CollisionWarningSystem:

    def __init__(self, warning_distance=30):
        self.warning_distance = warning_distance

    def check_warning(self, distance):

        if distance <= self.warning_distance:
            return "WARNING"
        return "SAFE"
