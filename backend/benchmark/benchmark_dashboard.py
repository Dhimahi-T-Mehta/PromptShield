import statistics
import time

import requests

URL = "http://localhost:8000/api/v1/dashboard/overview"

times = []

for _ in range(20):
    start = time.perf_counter()

    requests.get(URL)

    end = time.perf_counter()

    times.append((end - start) * 1000)

print(f"Average: {statistics.mean(times):.2f} ms")
print(f"Min: {min(times):.2f} ms")
print(f"Max: {max(times):.2f} ms")