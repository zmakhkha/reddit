# gtts_generator.py

import os
import json
from gtts import gTTS

def generate_audio_from_stories(story_folder="stories", output_folder="output_audio"):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(story_folder):
        if filename.endswith(".json"):
            filepath = os.path.join(story_folder, filename)
            subreddit_date = filename.replace("stories_", "").replace(".json", "")
            print(f"🎧 Generating MP3s for {subreddit_date}...")

            with open(filepath, "r", encoding="utf-8") as f:
                stories = json.load(f)

            for i, story in enumerate(stories, 1):
                title = story["title"].strip()
                body = story["story"].strip()
                text = f"{title}. {body}"

                tts = gTTS(text)
                clean_title = f"{subreddit_date}_story_{i}.mp3".replace(" ", "_")
                output_path = os.path.join(output_folder, clean_title)
                tts.save(output_path)

                print(f"✅ Saved: {output_path}")

if __name__ == "__main__":
    generate_audio_from_stories()
