import pytest
import pandas as pd
from pandas.testing import assert_frame_equal


def explode_grades_list(df: pd.DataFrame) -> pd.DataFrame: # noqa: F811
    if 'Grades' not in df.columns:
        raise KeyError("Input DataFrame must contain a 'Grades' column.")
    exploded = df.explode('Grades').rename(columns={'Grades': 'Grade'})
    return exploded.dropna(subset=['Grade'])


@pytest.fixture
def sample_dataframe():
    data = {
        'Student': ['Alice', 'Bob'],
        'Class': ['Math', 'History'],
        'Grades': [[90, 85], [78]]
    }
    return pd.DataFrame(data)


def test_basic_explosion_pytest(sample_dataframe):
    result_df = explode_grades_list(sample_dataframe).reset_index(drop=True)
    result_df["Grade"] = result_df["Grade"].astype(int)

    expected_df = pd.DataFrame({
        'Student': ['Alice', 'Alice', 'Bob'],
        'Class': ['Math', 'Math', 'History'],
        'Grade': [90, 85, 78]
    }).reset_index(drop=True)
    expected_df["Grade"] = expected_df["Grade"].astype(int)

    assert_frame_equal(result_df, expected_df) # noqa: F821


def test_with_empty_list_pytest():
    input_df = pd.DataFrame({
        'Student': ['Alice', 'Charlie'],
        'Grades': [[90, 85], []]
    })
    result_df = explode_grades_list(input_df).reset_index(drop=True)
    result_df["Grade"] = result_df["Grade"].astype(int)

    expected_df = pd.DataFrame({
        'Student': ['Alice', 'Alice'],
        'Grade': [90, 85]
    }).reset_index(drop=True)
    expected_df["Grade"] = expected_df["Grade"].astype(int)

    assert_frame_equal(result_df, expected_df) # noqa: F821


def test_missing_grades_column_raises_error_pytest():
    df = pd.DataFrame({'Student': ['David']})
    with pytest.raises(KeyError, match="Input DataFrame must contain a 'Grades' column."):
        explode_grades_list(df)
