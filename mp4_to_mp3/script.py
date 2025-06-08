import os
from moviepy.editor import VideoFileClip

def convert_all_mp4_to_mp3(input_dir='in', output_dir='out'):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # List all MP4 files in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.mp4'):
            mp4_path = os.path.join(input_dir, filename)
            mp3_name = os.path.splitext(filename)[0] + '.mp3'
            mp3_path = os.path.join(output_dir, mp3_name)

            print(f"Converting: {mp4_path} -> {mp3_path}")
            try:
                video = VideoFileClip(mp4_path)
                if video.audio:
                    video.audio.write_audiofile(mp3_path)
                else:
                    print(f"No audio found in {filename}. Skipping.")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
            finally:
                video.close()

if __name__ == "__main__":
    convert_all_mp4_to_mp3()
