import pandas as pd
import pytest
import sqlite3
import pandas.testing as pdt
from import_data import load_and_split_posts_csv
from database_setup import setup_database
from io import StringIO


def test_load_and_split_posts_csv():
    """
    Tests the load_and_split_posts_csv function with mock CSV data.
    """

    csv_content = """Post_id,Post_Type,comments,likes
101,Carousel,268,16382
102,Reel,138,9267
103,Reel,1089,10100
104,Reel,271,6943
105,Reel,145,17158
"""

    csv_file = StringIO(csv_content)

    expected_post_types = pd.DataFrame({
        'Post_id': [101, 102, 103, 104, 105],
        'Post_Type': pd.Categorical(['Carousel', 'Reel', 'Reel',
                                     'Reel', 'Reel'])
    })

    expected_post_comments = pd.DataFrame({
        'Post_id': [101, 102, 103, 104, 105],
        'comments': [268, 138, 1089, 271, 145]
    })

    expected_post_likes = pd.DataFrame({
        'Post_id': [101, 102, 103, 104, 105],
        'likes': [16382, 9267, 10100, 6943, 17158]
    })

    post_types_df, post_comments_df, post_likes_df = load_and_split_posts_csv(
        csv_file)

    pdt.assert_frame_equal(post_types_df, expected_post_types)
    pdt.assert_frame_equal(post_comments_df, expected_post_comments)
    pdt.assert_frame_equal(post_likes_df, expected_post_likes)

    assert post_types_df['Post_Type'].dtype.name == 'category'
    assert post_comments_df['comments'].dtype == 'int64'
    assert post_likes_df['likes'].dtype == 'int64'
