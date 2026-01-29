import pandas as pd

def clean_sensor_data(data: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicatas e garante que o timestamp seja datetime."""
    data = data.drop_duplicates()
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    # Criando uma feature simples: Razão Temperatura/Vibração
    data['temp_vib_ratio'] = data['temperature'] / (data['vibration'] + 0.001)
    return data