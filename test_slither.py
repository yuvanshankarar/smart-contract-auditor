import subprocess
import shutil

SLITHER = shutil.which("slither")

print("SLITHER:", SLITHER)

result = subprocess.run(
    [SLITHER, "--version"],
    capture_output=True,
    text=True
)

print("RETURN CODE:", result.returncode)
print("STDOUT:", repr(result.stdout))
print("STDERR:", repr(result.stderr))