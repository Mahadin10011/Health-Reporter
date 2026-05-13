from collector import collect_metrics
from analyser import analyse, load_config
from narrator import narrate
from reporter import write_report, notify_if_critical

print("Collecting metrics...")
metrics = collect_metrics()

print("Analysing...")
flags = analyse(metrics, load_config())

print("Generating narrative...")
narrative = narrate(metrics, flags)

print("Writing report...")
path = write_report(narrative, metrics, flags)

notify_if_critical(flags)
print(f"Done. Report saved to {path}")