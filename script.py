import praw
import json
from datetime import datetime

# Reddit API setup
reddit = praw.Reddit(
    client_id="sJZY-0l9-kjwEJ3ltRAQrg",
    client_secret="VzaOW0IOEnDwJG5xPZm0-UdFuFeyOA",
    user_agent="mks-stories-script by zakaria"
)

def save_stories_to_json(subreddit_name, limit=10):
    today_str = datetime.today().strftime("%Y-%m-%d")
    filename = f"stories_{subreddit_name}_{today_str}.json"

    subreddit = reddit.subreddit(subreddit_name)
    stories = []

    print(f"Fetching {limit} posts from r/{subreddit_name}...")

    for post in subreddit.top(limit=limit):
        stories.append({
            "title": post.title.strip(),
            "story": post.selftext.strip() if post.selftext else ""
        })

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(stories, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved to {filename}")

# Example usage
save_stories_to_json("SluttyConfessions", limit=5)
