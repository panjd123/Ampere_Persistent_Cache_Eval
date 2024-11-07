"""
l2 cache size: 41943040
max persisting cache size: 26214400 Byte
set persisting cache size: 10485760 Byte
window num_bytes: 10485760
window hit ratio: 1
Time: 3.696934 ms
Time: 7.424063 ms
"""

import subprocess
import pandas as pd
import seaborn as sns
from tqdm import tqdm
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--run", action="store_true")
parser.add_argument("--diag", action="store_true")
args = parser.parse_args()
run = args.run
diag = args.diag

if run:
    if not diag:
        datas = []
        total = 0
        for data_len in [4, 8, 12, 16, 20, 24, 28, 32, 40, 48, 56, 64, 80, 96]:
            for per_len in [1, 2, 4, 8, 12, 16, 20, 24, 28, 32, 40, 48]:
                if per_len > data_len:
                    continue
                total += 1

        pbar = tqdm(total=total)
        for data_len in [4, 8, 12, 16, 20, 24, 28, 32, 40, 48, 56, 64, 80, 96]:
            for per_len in [1, 2, 4, 8, 12, 16, 20, 24, 28, 32, 40, 48]:
                if per_len >= data_len:
                    continue
                res = subprocess.run(["./main", str(data_len), str(per_len), "100"], capture_output=True)
                output = res.stdout.decode()
                time1 = float(output.split("\n")[5].split(": ")[1].split(" ms")[0])
                time2 = float(output.split("\n")[6].split(": ")[1].split(" ms")[0])
                datas.append([data_len, per_len, time1, time2])
                
        df = pd.DataFrame(datas, columns=["data_len", "per_len", "time1", "time2"])
        df["speedup"] = df["time2"] / df["time1"]
        df.to_csv("data.csv", index=False)
    else:
        datas = []
        for data_len in tqdm([1, 2, 4, 8, 12, 16, 20, 21, 22, 23, 24, 25, 28, 32, 40, 48, 56, 64, 80, 96, 112, 128, 256, 386, 512, 1024]):
            for per_len in [data_len]:
                res = subprocess.run(["./main", str(data_len), str(per_len), "100"], capture_output=True)
                output = res.stdout.decode()
                time1 = float(output.split("\n")[5].split(": ")[1].split(" ms")[0])
                time2 = float(output.split("\n")[6].split(": ")[1].split(" ms")[0])
                datas.append([data_len, per_len, time1, time2])
        df = pd.DataFrame(datas, columns=["data_len", "per_len", "time1", "time2"])
        df["speedup"] = df["time2"] / df["time1"]
        df.to_csv("data_diag.csv", index=False)

if not diag:
    df = pd.read_csv("data.csv")
    sns.set_theme(style="whitegrid")
    # x, y, z = "data_len", "per_len", "speedup"

    # Draw a heatmap with the numeric values in each cell
    df.columns = ["total_data(MB)", "freq_data(MB)", "time1", "time2", "speedup"]
    f, ax = plt.subplots(figsize=(18, 12))
    pivot = df.pivot(index = "total_data(MB)", columns = "freq_data(MB)", values = "speedup")
    pivot = pivot[::-1]
    sns.heatmap(pivot, annot=True, fmt=".3f", linewidths=.5, ax=ax)
    plt.savefig("heatmap.png")
else:
    f, ax = plt.subplots(figsize=(18, 12))
    df = pd.read_csv("data_diag.csv")
    sns.set_theme(style="whitegrid")
    sns.lineplot(data=df, x="data_len", y="speedup", ax=ax)
    # xlog
    plt.xscale("log")
    ticks = [1, 2, 4, 8, 12, 16, 20, 21, 22, 23, 24, 25, 28, 32, 40, 48, 56, 64, 80, 96, 112, 128, 256, 386, 512, 1024]
    plt.xticks(ticks, ticks)
    plt.savefig("diag.png")
