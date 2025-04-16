import ast

def read_stats(file_path):
    means = []
    stds = []

    with open(file_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        try:
            mean, std = ast.literal_eval(line.strip())
            means.append(mean)
            stds.append(std)
        except Exception as e:
            print(f"Skipping line due to parse error: {line.strip()} | Error: {e}")

    return means, stds

def compute_average(stat_list):
    import numpy as np
    arr = np.array(stat_list)
    return arr.mean(axis=0).tolist()

def summarize(file_path):
    means, stds = read_stats(file_path)
    avg_mean = compute_average(means)
    avg_std = compute_average(stds)

    print(f"\n📄 File: {file_path}")
    print(f"▶️ Average Mean: {avg_mean}")
    print(f"▶️ Average Std : {avg_std}")

if __name__ == "__main__":
    # Run on both files
    summarize("rgb_latent_norm_params.csv")
    summarize("motion_latent_norm_params.csv")
    summarize("rgb_latent_norm_after.csv")
    summarize("motion_latent_norm_after.csv")