class SensorFusion:

    def fuse(self, radar_distance, camera_detection):

        # Radar detected object and camera confirms it
        if radar_distance is not None and camera_detection:
            return "Obstacle Confirmed"

        # Only one sensor detects object
        if radar_distance is not None or camera_detection:
            return "Possible Obstacle"

        # No sensor detects object
        return "No Obstacle"
