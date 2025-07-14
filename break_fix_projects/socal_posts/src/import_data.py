import pandas as pd
from typing import Tuple, Dict, Optional


def load_and_split_posts_csv(
    filepath: str,
    dtypes: Optional[Dict[str, str]] = None
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Load posts CSV with explicit dtypes and split into 3 DataFrames.

    Args:
        filepath (str): Path to the CSV file.
        dtypes (Optional[Dict[str, str]]): Dict of column dtypes to enforce.
        Defaults to None.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
            DataFrames for Post_Types, Post_Comments, and Post_Likes tables.
    """
    if dtypes is None:
        dtypes = {
            'Post_id': 'int64',
            'Post_Type': 'category',
            'comments': 'int64',
            'likes': 'int64'
        }

    data: pd.DataFrame = pd.read_csv(filepath, dtype=dtypes)

    post_types_df: pd.DataFrame = data[['Post_id', 'Post_Type']].copy()
    post_comments_df: pd.DataFrame = data[['Post_id', 'comments']].copy()
    post_likes_df: pd.DataFrame = data[['Post_id', 'likes']].copy()

    return post_types_df, post_comments_df, post_likes_df


if __name__ == "__main__":
    post_types_df, post_comments_df, post_likes_df = load_and_split_posts_csv(
        'break_fix_projects/Socal_posts/data/posts.csv')
    print("Post Types DataFrame:")
    print(post_types_df.head())
    print("\nPost Comments DataFrame:")
    print(post_comments_df.head())
    print("\nPost Likes DataFrame:")
    print(post_likes_df.head())
