import sqlite3
import os
import pandas as pd
from import_data import load_and_split_posts_csv


def initialize_schema(conn: sqlite3.Connection):
    """
    Drops existing tables and creates a new schema.

    Args:
        conn: An active sqlite3 connection object.
    """
    cursor = conn.cursor()

    tables_to_drop = ["Post_Types", "Post_Comments", "Post_Likes"]
    for table in tables_to_drop:
        cursor.execute(f"DROP TABLE IF EXISTS {table}")

    cursor.execute("""
    CREATE TABLE Post_Types (
        Post_id INTEGER PRIMARY KEY,
        Post_Type TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE Post_Comments (
        Post_id INTEGER PRIMARY KEY,
        comments INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE Post_Likes (
        Post_id INTEGER PRIMARY KEY,
        likes INTEGER
    )
    """)
    print("Database schema initialized.")


def populate_tables(conn: sqlite3.Connection,
                    post_types_df: pd.DataFrame,
                    post_comments_df: pd.DataFrame,
                    post_likes_df: pd.DataFrame):
    """
    Populates the database tables from pandas DataFrames.

    Args:
        conn: An active sqlite3 connection object.
        post_types_df: DataFrame for Post_Types table.
        post_comments_df: DataFrame for Post_Comments table.
        post_likes_df: DataFrame for Post_Likes table.
    """
    post_types_df.to_sql('Post_Types', conn, if_exists='append', index=False)
    post_comments_df.to_sql('Post_Comments', conn,
                            if_exists='append', index=False)
    post_likes_df.to_sql('Post_Likes', conn, if_exists='append', index=False)
    print("Tables populated successfully.")


def setup_database(db_path: str,
                   post_types_df: pd.DataFrame,
                   post_comments_df: pd.DataFrame,
                   post_likes_df: pd.DataFrame):
    """
    A complete function to connect, initialize, and populate the database.

    Args:
        db_path: The file path for the SQLite database.
        post_types_df: DataFrame for Post_Types table.
        post_comments_df: DataFrame for Post_Comments table.
        post_likes_df: DataFrame for Post_Likes table.
    """
    try:
        with sqlite3.connect(db_path) as conn:
            initialize_schema(conn)
            populate_tables(conn, post_types_df,
                            post_comments_df, post_likes_df)
        print(f"Database '{db_path}' setup complete.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to execute the database setup.
    """
    csv_file = "../data/posts.csv"
    post_types_df, post_comments_df, post_likes_df = \
        load_and_split_posts_csv(csv_file)

    db_path = "database/social_posts.db"

    db_dir = os.path.dirname(db_path)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
        print(f"Created directory: {db_dir}")

    setup_database(db_path, post_types_df, post_comments_df, post_likes_df)


if __name__ == "__main__":
    main()
