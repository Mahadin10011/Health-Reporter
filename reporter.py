import pathlib, datetime
from plyer import notification

def write_report(narrative, metrics, flags):
    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    path = pathlib.Path("reports") / f"health_{ts}.md"
    path.parent.mkdir(exist_ok=True)
    content = f"# System Health Report\n**Generated:** {ts}\n\n{narrative}"
    path.write_text(content)
    print(f"Report written to {path}")
    return path

def notify_if_critical(flags):
    critical = [f for f in flags if f["severity"] == "critical"]
    if critical:
        notification.notify(
            title="System Health Alert",
            message=f"{len(critical)} critical issue(s) detected. Check your report.",
            timeout=10
        )

if __name__ == "__main__":
    from collector import collect_metrics
    from analyser import analyse, load_config
    metrics = collect_metrics()
    flags = analyse(metrics, load_config())
    narrative = "Test report — narrator skipped for now."
    path = write_report(narrative, metrics, flags)
    notify_if_critical(flags)