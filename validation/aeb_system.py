class AEBSystem:

    def __init__(self, threshold=2):
        self.threshold = threshold


    def check_braking(self, ttc):

        if ttc <= self.threshold:
            return "BRAKE"

        return "NO_BRAKE"
