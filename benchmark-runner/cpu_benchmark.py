import time
import json
import os
import socket
from datetime import datetime

ITERATIONS = int(os.getenv("ITERATIONS", "50000000"))

start = time.time()

x = 0
for i in range(ITERATIONS):
    x += i % 7

end = time.time()

result = {
    "benchmark": "cpu-loop",
    "iterations": ITERATIONS,
    "duration_sec": round(end - start, 3),
    "cpu_count": os.cpu_count(),
    "hostname": socket.gethostname(),
    "timestamp": datetime.utcnow().isoformat() + "Z"
}

print(json.dumps(result, indent=2))
