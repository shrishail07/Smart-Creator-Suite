import streamlit as st

from media_tools import compress_video, trim_audio
from backup_tool import backup_folder, compress_folder, restore_backup
from system_dashboard import get_system_stats, plot_graph
from file_watcher import start_watcher

st.set_page_config(page_title="Smart Creator Suite", layout="wide")

st.title("🎬 Smart Creator Suite")

# ---------------- VIDEO ----------------
st.header("📹 Video Compression")

video_input = st.text_input("Input Video Path")
video_output = st.text_input("Output Video Path")

if st.button("Compress Video"):
    msg = compress_video(video_input, video_output)
    st.success(msg)


# ---------------- AUDIO ----------------
st.header("🎵 Audio Trimming")

audio_input = st.text_input("Input Audio Path")
audio_output = st.text_input("Output Audio Path")

start_ms = st.number_input("Start Time (ms)", value=0)
end_ms = st.number_input("End Time (ms)", value=5000)

if st.button("Trim Audio"):
    msg = trim_audio(audio_input, audio_output, start_ms, end_ms)
    st.success(msg)


# ---------------- BACKUP ----------------
st.header("📦 Backup Tools")

source = st.text_input("Source Folder")
destination = st.text_input("Destination Folder")

if st.button("Backup Folder"):
    path = backup_folder(source, destination)
    st.success(f"Backup created at: {path}")

if st.button("Compress Folder"):
    zip_path = compress_folder(source)
    st.success(f"Compressed at: {zip_path}")


# ---------------- SYSTEM ----------------
st.header("📊 System Dashboard")

stats = get_system_stats()
st.json(stats)


# ---------------- FILE WATCHER ----------------
st.header("👀 File Watcher")

source_watch = st.text_input("Watch Folder")
target_watch = st.text_input("Move To Folder")

if st.button("Start Watcher"):
    observer = start_watcher(source_watch, target_watch)
    st.success("Watcher started!")
