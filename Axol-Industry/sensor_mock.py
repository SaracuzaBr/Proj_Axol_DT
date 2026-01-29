import requests
import time
import random

API_URL = "http://127.0.0.1:8000/readings"

def run_simulator():
    print("🚜 Simulador Industrial Nexus iniciado...")
    machines = ["Moinho-01", "Torno-05", "Esteira-02"]
    
    while True:
        for machine in machines:
            payload = {
                "machine_id": machine,
                "temperature": round(random.uniform(30.0, 90.0), 2),
                "vibration": round(random.uniform(0.1, 2.5), 4)
            }
            try:
                response = requests.post(API_URL, json=payload)
                print(f"✅ [{machine}] Enviado: {payload} | Status: {response.status_code}")
            except Exception as e:
                print(f"❌ Erro de conexão: {e}")
        
        time.sleep(3) # Envia novos dados a cada 3 segundos

if __name__ == "__main__":
    run_simulator()