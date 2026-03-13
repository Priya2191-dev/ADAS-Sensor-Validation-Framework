class TimeToCollision:

    def calculate_ttc(self, distance, speed):

        if speed == 0:
            return float("inf")

        return distance / speed


    def evaluate_risk(self, ttc):

        if ttc < 2:
            return "CRITICAL"

        elif ttc < 4:
            return "WARNING"

        return "SAFE"
