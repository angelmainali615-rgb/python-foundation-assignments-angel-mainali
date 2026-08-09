# Exercise 5: Pipeline Health Status

test_cases = [
    {
        "rows_loaded": 9800,
        "rows_failed": 200,
        "runtime_minutes": 18
    },
    {
        "rows_loaded": 9500,
        "rows_failed": 500,
        "runtime_minutes": 15
    },
    {
        "rows_loaded": 9900,
        "rows_failed": 100,
        "runtime_minutes": 30
    }
]

for case in test_cases:
    rows_loaded = case["rows_loaded"]
    rows_failed = case["rows_failed"]
    runtime_minutes = case["runtime_minutes"]

    # Calculate total rows
    total_rows = rows_loaded + rows_failed

    # Calculate failure rate
    failure_rate = (rows_failed / total_rows) * 100

    # Determine pipeline status
    if failure_rate <= 2 and runtime_minutes <= 20:
        status = "Healthy"
    elif failure_rate <= 5:
        status = "Warning"
    else:
        status = "Critical"

    # Display result
    print(f"Rows loaded: {rows_loaded}")
    print(f"Rows failed: {rows_failed}")
    print(f"Runtime: {runtime_minutes} minutes")
    print(f"Failure rate: {failure_rate:.2f}%")
    print(f"Pipeline status: {status}")
    print("-" * 40)