import timeit
import pandas as pd


def build_dataframe(num, time_results, results_list):
    row = {"N": num}
    for idx, t in enumerate(time_results, start=1):
        row[f"run_{idx}"] = t
    results_list.append(row)

def print_individual_results(num, time_results):
    avg = sum(time_results) / len(time_results)
    print(f"N={num}")
    print(f"  runs: {['{:.6f}'.format(t) for t in time_results]}")
    print(f"  min={min(time_results):.6f}, avg={avg:.6f}, max={max(time_results):.6f}\n")


setup = "lst = []"
stmt = """
for i in range(N):
    lst.append(i)
""".strip()
results = []

for N in (10**5, 10**6, 10**7):
    times = timeit.repeat(
        stmt.format(N=N),
        setup=setup,
        repeat=5,  # run the whole loop 5 times
        number=1,  # each repeat executes it once
        globals=globals()
    )
    build_dataframe(N, times, results)
    print_individual_results(N, times)

df = pd.DataFrame(results)
print(df)

