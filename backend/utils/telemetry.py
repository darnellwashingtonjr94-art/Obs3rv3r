import time

class MetricsCollector:
    def __init__(self):
        self.metrics = []

    def log_latency(self, agent_name: str, start_time: float):
        latency = time.time() - start_time
        self.metrics.append({"agent": agent_name, "latency_ms": round(latency * 1000, 2)})
