import timeit
import pandas as pd
import numpy as np
import json

PROBLEM_SIZES = [100_000, 1_000_000, 10_000_000]
METHODS = {
    "append": "lst = []\nfor i in range({n}): lst.append(i)",
    "comprehension": "lst = [i for i in range({n})]",
    "numpy_array": "arr = np.arange({n})",
    "numpy_to_list": "lst = np.arange({n}).tolist()",
    "generator": "lst = list((i for i in range({n})))"
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

# Analysis functions
def create_min_df(input_df: pd.DataFrame) -> pd.DataFrame:
    run_cols = [col for col in input_df.columns if col.startswith('run_')]
    return (input_df
            .assign(min_time=lambda d: d[run_cols].min(axis=1))
            [['N', 'method', 'min_time']])

def pivot_min_df(input_df: pd.DataFrame) -> pd.DataFrame:
    return (input_df.pivot(index='N', columns='method', values='min_time')
            .reset_index())

def export_min_chart_json(input_df: pd.DataFrame) -> None:
    labels = input_df['N'].to_list()
    datasets = [
        {'label': col,
         'data': input_df[col].to_list(),
         'fill': False,
         'borderWidth': 2
        }
        for col in input_df.columns if col != 'N'
    ]

    chart_data = {
        'labels': labels,
        'datasets': datasets
    }

    with open('./experiments/list_growth/min_chart_data.json', 'w') as f:
        json.dump(chart_data, f)

if __name__ == "__main__":
    results = []
    for method, statement in METHODS.items():
        results.extend(measure(method, statement, PROBLEM_SIZES))
    df = pd.DataFrame(results)
    print(df, '\n')
    df_min = create_min_df(df)
    df_plot = pivot_min_df(df_min)
    print(df_plot, '\n')
    export_min_chart_json(df_plot)


