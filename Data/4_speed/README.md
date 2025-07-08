# Writing Efficient Code: A Practical Exploration

In this section, we explore strategies for writing **more efficient, readable, and scalable Python code**. By leveraging tools like `%%timeit`, we’ll measure and compare execution times directly within Jupyter notebooks to gain insight into how different approaches affect performance.

These examples are not about micro-optimizations—but rather about building good habits early. While some differences in speed may seem trivial in isolation, they can scale dramatically in real-world data workflows, and production environments. Over time, even modest performance gains can lead to substantial savings in processing power, execution time, and infrastructure costs—ultimately translating into real financial impact.


---

## Notebook Overview

| Notebook         | Description |
|------------------|-------------|
| **1_speed.ipynb** | We examine how performance changes when evolving a solution from a simple one-liner, to a function, and then into a class. We’ll measure each step and discuss the trade-offs of speed vs. maintainability. |
| **2_data.ipynb**  | We explore the impact of data types in pandas, and how choosing the right types can reduce memory usage and speed up operations—especially important in large-scale data projects. |

---

## Key Takeaways

- Even small improvements in efficiency can add up at scale.
- Writing clean, modular code is often more valuable than shaving off microseconds.
- Understanding performance trade-offs helps you make better design decisions.
- Tools like `%%timeit`, `memory_usage`, and type inspection are essential for writing performant data science code.

## Other files 
- `data_maker.py` - used to make sample data to play with 
- `plot_tool.py` - used to make plots in the notebook.
- `lil_data.csv` - sample data for files
- `my_tricky_data.csv` - sample data for files

# Pandas Data Types Cheat Sheet

Optimize performance and memory in your data analysis by explicitly setting column types.

---

## Numeric Types

| Pandas dtype | Python equivalent | When to use                     | Memory-efficient? |
|--------------|--------------------|----------------------------------|--------------------|
| `int64`      | `int`              | Default for integers             | ❌ No              |
| `int32`      | `int`              | Smaller integers (±2B)           | ✅ Yes             |
| `int8`       | `int`              | Small values or flags (0/1)      | ✅ Yes             |
| `float64`    | `float`            | Default for floats               | ❌ No              |
| `float32`    | `float`            | Lower-precision floats           | ✅ Yes             |
| `float16`    | `float`            | Large arrays, limited precision  | ✅⚠️ Yes           |

---

## String and Categorical

| Pandas dtype | When to use                              | Notes                          |
|--------------|-------------------------------------------|--------------------------------|
| `object`     | Default for strings/mixed types           | ❌ Slow, memory-heavy          |
| `string`     | New dedicated string type                 | Safer than `object`           |
| `category`   | Repeating text values (e.g. country)      | ✅ Great for groupby/filtering |

```python
df["gender"] = df["gender"].astype("category")
```

---

## Date/Time

| Pandas dtype      | When to use               | Notes                     |
|-------------------|----------------------------|---------------------------|
| `datetime64[ns]`  | Date/time values           | Use `pd.to_datetime()`    |
| `timedelta64[ns]` | Durations or differences   | Use `pd.to_timedelta()`   |

```python
df["date"] = pd.to_datetime(df["date"], errors="coerce")
```

---

## Boolean

| Pandas dtype | When to use        | Notes                          |
|--------------|--------------------|--------------------------------|
| `bool`       | True/False          | ✅ Very efficient               |
| `boolean`    | With missing values | Use for nullable booleans      |

```python
df["is_active"] = df["is_active"].astype("bool")
```

---

## Pro Tips

- **Set types when loading CSVs**
```python
pd.read_csv("file.csv", dtype={"id": "int32", "gender": "category"})
```

- **Downcast numerics**
```python
df["score"] = pd.to_numeric(df["score"], downcast="float")
df["id"] = pd.to_numeric(df["id"], downcast="integer")
```

- **Check memory usage**
```python
df.info(memory_usage="deep")
```

---

## Summary Table

| Column Type | Best dtype         | Why                          |
|-------------|--------------------|-------------------------------|
| IDs         | `int32`/`int64`    | Save memory, keep accuracy    |
| Flags       | `bool`/`int8`      | Small and efficient           |
| Categories  | `category`         | Speeds up groupby/filtering   |
| Prices      | `float32`          | Good enough for most floats   |
| Dates       | `datetime64[ns]`   | Enables time-based filtering  |
| Short text  | `category`/`string`| Faster than `object`          |
| Long text   | `object`           | Only real option (for now)    |

---

> Use `astype()` or `dtype=` to control types and avoid surprises.