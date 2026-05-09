try:
    from moviepy.editor import VideoFileClip
except ImportError:
    from moviepy import VideoFileClip

import subprocess


def compress_video(input_path, output_path):

    video = VideoFileClip(input_path)

    video.write_videofile(output_path, bitrate="500k")

    video.close()

    return "Video Compressed Successfully"


def trim_audio(input_path, output_path, start_ms, end_ms):

    start_sec = start_ms / 1000
    duration = (end_ms - start_ms) / 1000

    command = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-ss", str(start_sec),
        "-t", str(duration),
        output_path
    ]

    subprocess.run(command)

    return "Audio Trimmed Successfully"
