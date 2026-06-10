import subprocess
import shutil

SLITHER = shutil.which("slither")


def run_slither(contract_path):

    cmd = f'"{SLITHER}" "{contract_path}"'

    print("COMMAND:", cmd)

    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )

    print("RETURN CODE:", result.returncode)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    return result.stdout