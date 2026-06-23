from monitor import Monitor, ComponentMetrics

def test_collect_metrics():
    monitor = Monitor()
    monitor.collect_metrics("component1", {"cpu": 50, "memory": 60, "error_rate": 3})
    assert monitor.metrics["component1"].cpu == 50
    assert monitor.metrics["component1"].memory == 60
    assert monitor.metrics["component1"].error_rate == 3

def test_get_component_health_green():
    monitor = Monitor()
    monitor.collect_metrics("component1", {"cpu": 50, "memory": 60, "error_rate": 3})
    assert monitor.get_component_health("component1") == "green"

def test_get_component_health_yellow():
    monitor = Monitor()
    monitor.collect_metrics("component1", {"cpu": 90, "memory": 60, "error_rate": 3})
    assert monitor.get_component_health("component1") == "yellow"

def test_get_component_health_red():
    monitor = Monitor()
    monitor.collect_metrics("component1", {"cpu": 50, "memory": 60, "error_rate": 6})
    assert monitor.get_component_health("component1") == "red"

def test_send_alert():
    monitor = Monitor()
    monitor.collect_metrics("component1", {"cpu": 50, "memory": 60, "error_rate": 6})
    monitor.send_alert("component1")
    # No assertion, just checking it runs without error

def test_get_dashboard():
    monitor = Monitor()
    monitor.collect_metrics("component1", {"cpu": 50, "memory": 60, "error_rate": 3})
    monitor.collect_metrics("component2", {"cpu": 90, "memory": 60, "error_rate": 6})
    dashboard = monitor.get_dashboard()
    assert dashboard["component1"] == "green"
    assert dashboard["component2"] == "red"
