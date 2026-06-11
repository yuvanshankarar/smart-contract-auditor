import subprocess
import json
import shutil

SLITHER = shutil.which("slither")


def run_slither(contract_path):

    cmd = [
        SLITHER,
        contract_path,
        "--json",
        "-"
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    # Windows Slither sometimes returns a bad exit code
    # even when valid JSON is produced.

    if result.stdout.strip():

        try:
            return json.loads(result.stdout)
        except Exception:
            pass

    raise Exception(
        f"Slither failed\n"
        f"Return code: {result.returncode}\n"
        f"STDERR: {result.stderr}"
    )