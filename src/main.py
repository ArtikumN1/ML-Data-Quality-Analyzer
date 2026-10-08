from data_loader import load_csv
from profiler import DatasetProfiler
from pprint import pprint
from validators.missing import check_missing
from validators.numeric import check_numeric

df = load_csv("data/raw/example.csv")

profiler = DatasetProfiler(df)

basic_info = profiler.get_basic_info()
dtypes = profiler.get_dtypes()
feature_types = profiler.detect_feature_types()
missing_report = check_missing(df)
numeric_report = check_numeric(df)

print("BASIC INFO")
pprint(basic_info)

print("\nDATA TYPES")
pprint(dtypes)

print("\nFEATURE TYPES")

for column, feature_type in feature_types.items():
    print(f"{column}: {feature_type}")

print("\nMISSING VALUES")

for column, info in missing_report.items():
    print(
        f"{column}: "
        f"{info['count']} missing "
        f"({info['percentage']}%)"
    )

print("\nNUMERIC ISSUES")

for column, issues in numeric_report.items():
    print(f"{column}:")