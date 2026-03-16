import re
from collections import Counter

def analyze_logs(log_lines):

    error_count = 0
    warning_count = 0
    services = []

    for line in log_lines:

        if "ERROR" in line:
            error_count += 1

        if "WARN" in line:
            warning_count += 1

        if "service=" in line:
            svc = line.split("service=")[1].split()[0]
            services.append(svc)

    service_counts = Counter(services)

    return {
        "total_logs": len(log_lines),
        "errors": error_count,
        "warnings": warning_count,
        "top_services": service_counts.most_common(5)
    }