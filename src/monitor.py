import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ComponentMetrics:
    cpu: float
    memory: float
    error_rate: float

class Monitor:
    def __init__(self):
        self.metrics = {}

    def collect_metrics(self, component: str, metrics: Dict[str, float]) -> None:
        self.metrics[component] = ComponentMetrics(**metrics)

    def get_component_health(self, component: str) -> str:
        if component not in self.metrics:
            return "unknown"
        metrics = self.metrics[component]
        if metrics.error_rate > 5:
            return "red"
        elif metrics.cpu > 80 or metrics.memory > 80:
            return "yellow"
        else:
            return "green"

    def send_alert(self, component: str) -> None:
        if self.get_component_health(component) == "red":
            print(f"Sending alert for {component}")

    def get_dashboard(self) -> Dict[str, str]:
        return {component: self.get_component_health(component) for component in self.metrics}
