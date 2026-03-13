import pandas as pd

class SensorDataValidator:

    def validate_sensor_data(self, file):

        data = pd.read_csv(file)

        if data.isnull().sum().sum() > 0:
            return False

        return True
