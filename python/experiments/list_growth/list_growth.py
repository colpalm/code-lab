import timeit
import pandas as pd

PROBLEM_SIZES = [100_000, 1_000_000, 10_000_000]
METHODS = {
    "append": "lst = []\nfor i in range({n}): lst.append(i)",
    "comprehension": "lst = [i for i in range({n})]"
}

def measure(method_name: str, statement_template: str, problem_sizes: list[int], repeat: int = 5) -> list[dict]:
    rows = []
    for size in problem_sizes:
        stmt = statement_template.format(n=size)
        setup = ""
        times = timeit.repeat(stmt, setup, repeat=repeat, number=1, globals=globals())

        # Transfer to dict
        row = construct_row(size, method_name, times)
        rows.append(row)
    return rows

def construct_row(n, method_identifier, times) -> dict:
    r = {"N": n, "method": method_identifier}
    for idx, t in enumerate(times, start=1):
        r[f"run_{idx}"] = t
    return r

if __name__ == "__main__":
    results = []
    for method, statement in METHODS.items():
        results.extend(measure(method, statement, PROBLEM_SIZES))
    df = pd.DataFrame(results)
    print(df)

