import subprocess
import shutil

SLITHER = shutil.which("slither")

if SLITHER is None:
    raise FileNotFoundError("slither not found in PATH")

path = "C:/smart_auditor/reentrancy.sol"

result = subprocess.run(
    [SLITHER, path],
    capture_output=True,
    text=True
)

print("RETURN CODE:", result.returncode)
print("STDOUT:")
print(result.stdout)
print("STDERR:")
print(result.stderr)