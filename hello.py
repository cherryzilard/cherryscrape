import os
from datetime import datetime, timezone

os.makedirs("output", exist_ok=True)
msg = f"Hello, World from a container! {datetime.now(timezone.utc).isoformat()}"

with open("output/hello.txt", "w") as f:
    f.write(msg + "\n")

print(msg)
