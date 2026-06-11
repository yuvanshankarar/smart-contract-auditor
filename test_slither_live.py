from app.analyzers.slither_analyzer import run_slither
from app.analyzers.slither_parser import parse_slither_output

report = run_slither("contracts/reentrancy.sol")

print("RAW REPORT:")
print(report)

print("\nPARSED FINDINGS:")
print(parse_slither_output(report))