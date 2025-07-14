'''
Read in the json file containing social media posts, and perform the following tasks:

1. Find the post with the most comments:
How can you find the row with the highest number in the comments column?
Hint: Use .sort_values() and .head()
Then print the result with the text "Most Commented Post:" 
followed by the row data.

2. Find the post with the most likes:
How can you find the row with the highest number in the likes column?
Hint: Use .sort_values() and .head()
Then print the result with the text "Most Liked Post:" followed by the row data.

3. Find the most common post type:
How can you find which post_type appears most often?
Hint: Use .value_counts() and .head()
Then print the result with the text "Most Popular Post Type:" followed by the value counts.

4. Add up likes and comments for each post type:
How can you group the data by post_type and add the likes and comments?
Hint: Use .groupby() and .agg()
Then print the result with the text "Total Likes and Comments by Post Type:".

5. Print the totals nicely:
How can you print the grouped data without row numbers?
Hint: Use .to_string(index=False) inside the print().

6. Make a bar chart:
How can you create a bar chart to compare likes and comments by post type?
Hint: Use .plot(kind='bar') with the correct x and y parameters, and add title and size.

7. Make your output easy to read:
How can you add clear headings before each output and separate them?
Hint: Use print() with a string before each result and add blank lines after.
'''

import pandas as pd
import matplotlib.pyplot as plt


def get_most_commented_post(data: pd.DataFrame) -> pd.DataFrame:
    """
    Return the post with the highest number of comments.

    Args:
        data (pd.DataFrame): DataFrame containing post data.

    Returns:
        pd.DataFrame: Single-row DataFrame with the most commented post.
    """
    return data.sort_values(by='comments', ascending=False).head(1)


def print_most_commented_post(data: pd.DataFrame) -> None:
    """
    Print the most commented post with a header.

    Args:
        data (pd.DataFrame): DataFrame containing post data.
    """
    post = get_most_commented_post(data)
    print("Most Commented Post:")
    print(post.to_string(index=False), "\n")


def get_most_liked_post(data: pd.DataFrame) -> pd.DataFrame:
    """
    Return the post with the highest number of likes.

    Args:
        data (pd.DataFrame): DataFrame containing post data.

    Returns:
        pd.DataFrame: Single-row DataFrame with the most liked post.
    """
    return data.sort_values(by='likes', ascending=False).head(1)


def print_most_liked_post(data: pd.DataFrame) -> None:
    """
    Print the most liked post with a header.

    Args:
        data (pd.DataFrame): DataFrame containing post data.
    """
    post = get_most_liked_post(data)
    print("Most Liked Post:")
    print(post.to_string(index=False), "\n")


def get_most_popular_post_type(data: pd.DataFrame) -> pd.Series:
    """
    Return the most common post type and its count.

    Args:
        data (pd.DataFrame): DataFrame containing post data.

    Returns:
        pd.Series: Series with the most popular post type and count.
    """
    return data['post_type'].value_counts().head(1)


def print_most_popular_post_type(data: pd.DataFrame) -> None:
    """
    Print the most popular post type with a header.

    Args:
        data (pd.DataFrame): DataFrame containing post data.
    """
    popular = get_most_popular_post_type(data)
    print("Most Popular Post Type:")
    print(popular.to_string(), "\n")


def get_likes_comments_by_post_type(data: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate total likes and comments by post type.

    Args:
        data (pd.DataFrame): DataFrame containing post data.

    Returns:
        pd.DataFrame: DataFrame with post_type and sums of likes and comments.
    """
    return data.groupby('post_type').agg({'likes': 'sum', 'comments': 'sum'}).reset_index()


def print_likes_comments_by_post_type(data: pd.DataFrame) -> None:
    """
    Print total likes and comments by post type with a header.

    Args:
        data (pd.DataFrame): DataFrame containing post data.
    """
    agg = get_likes_comments_by_post_type(data)
    print("Total Likes and Comments by Post Type:")
    print(agg.to_string(index=False), "\n")


def plot_likes_comments_by_post_type(data: pd.DataFrame) -> None:
    """
    Plot a bar chart of likes and comments by post type.

    Args:
        data (pd.DataFrame): DataFrame containing post data.
    """
    agg = get_likes_comments_by_post_type(data)
    agg.plot(
        x='post_type',
        y=['likes', 'comments'],
        kind='bar',
        figsize=(10, 6),
        title='Likes and Comments by Post Type'
    )
    plt.show()


def main():
    # Load the data
    data = pd.read_json('/Users/dannymorton/Desktop/postGrad/CY_post_grad_data/break_fix_projects/socal_posts/data/posts.json')

    # Print the most commented post
    print_most_commented_post(data)

    # Print the most liked post
    print_most_liked_post(data)

    # Print the most popular post type
    print_most_popular_post_type(data)

    # Print total likes and comments by post type
    print_likes_comments_by_post_type(data)

    # Plot likes and comments by post type
    plot_likes_comments_by_post_type(data)


if __name__ == "__main__":
    main()
