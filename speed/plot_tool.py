import matplotlib.pyplot as plt
import re


def plot_benchmark_results(standard_import_time, dtype_import_time, standard_memory_usage, dtype_memory_usage):
    """
    Parses time and memory strings, then generates comparison plots.

    Args:
        standard_import_time (str): The raw output from timeit for the standard read.
                                    Example: "1.29 s ± 15.7 ms per loop..."
        dtype_import_time (str): The raw output from timeit for the dtype read.
                                 Example: "1.27 s ± 6.46 ms per loop..."
        standard_memory_usage (str): The memory usage string for the standard read.
                                     Example: "memory usage: 1.2 GB"
        dtype_memory_usage (str): The memory usage string for the dtype read.
                                  Example: "memory usage: 663.1 MB"
    """
    print("Parsing results and generating plots...")

    def _parse_memory(mem_string):
        match = re.search(r"([\d.]+)\s*([a-zA-Z]+)", mem_string)
        if not match:
            raise ValueError(f"Could not parse memory string: {mem_string}")

        value_str, unit = match.groups()
        value = float(value_str)

        if unit.upper() == 'GB':
            return value * 1024  # Convert GB to MB
        elif unit.upper() == 'KB':
            return value / 1024  # Convert KB to MB
        return value  # Assume MB

    try:
        # Extract the first number from the time strings
        time_std = float(standard_import_time.split(' ')[0])
        time_dtype = float(dtype_import_time.split(' ')[0])

        # Parse memory strings using the helper function
        mem_std = _parse_memory(standard_memory_usage)
        mem_dtype = _parse_memory(dtype_memory_usage)

    except (ValueError, IndexError) as e:
        print(f"Error parsing input strings: {e}")
        print("Please ensure the strings are copied correctly from the notebook output.")
        return

    load_times = {'Standard Read': time_std, 'Dtype Read': time_dtype}
    memory_usage = {'Inferred Dtypes': mem_std, 'Specified Dtypes': mem_dtype}

    plt.style.use('seaborn-v0_8-whitegrid')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Plot 1: Load Time
    labels1, times = load_times.keys(), load_times.values()
    bars1 = ax1.bar(labels1, times, color=['#ff9999', '#66b3ff'], width=0.6)
    ax1.set_title('CSV Read Time Comparison', fontsize=16, fontweight='bold')
    ax1.set_ylabel('Time (seconds)', fontsize=12)
    ax1.set_ylim(0, max(times) * 1.2)
    ax1.grid(axis='x')
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + (max(times)
                 * 0.01), f'{yval:.3f} s', ha='center', va='bottom', fontsize=11)

    # Plot 2: Memory Usage
    labels2, memory = memory_usage.keys(), memory_usage.values()
    bars2 = ax2.bar(labels2, memory, color=['#ff9999', '#66b3ff'], width=0.6)
    ax2.set_title('DataFrame Memory Usage Comparison',
                  fontsize=16, fontweight='bold')
    ax2.set_ylabel('Memory (MB)', fontsize=12)
    ax2.set_ylim(0, max(memory) * 1.2)
    ax2.grid(axis='x')
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + (max(memory) * 0.01),
                 f'{int(yval)} MB', ha='center', va='bottom', fontsize=11)

    fig.suptitle(
        'Impact of Specifying Dtypes on Pandas Performance', fontsize=20, y=1.03)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()


if __name__ == '__main__':
    # 1. You would copy and paste the output from your notebook here
    standard_import = "1.29 s ± 15.7 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)"
    dtype_import = "1.27 s ± 6.46 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)"
    standard_import_memory = "memory usage: 1.2 GB"
    dtype_import_memory = "memory usage: 663.1 MB"

    # 2. Then you would just call the function with your data
    plot_benchmark_results(standard_import, dtype_import,
                           standard_import_memory, dtype_import_memory)
