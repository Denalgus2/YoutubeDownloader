from pytube import YouTube
import os
from moviepy.editor import *

# Create the directory if it doesn't exist
output_directory = './clips'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# YouTube video URL

video_url = input("Enter the youtube video url: ")

# Download video and audio
yt = YouTube(video_url)


video_stream = yt.streams.order_by('resolution').desc().first()
audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()

print(video_stream)

# Download video and audio
video_stream.download(output_directory, filename='video.mp4')
audio_stream.download(output_directory, filename='audio.mp4')


#merge audio and video

while True:
    if os.path.exists(output_directory + '/video.mp4') and os.path.exists(output_directory + '/audio.mp4'):
        break
videoclip = VideoFileClip(output_directory + "/video.mp4")
audioclip = AudioFileClip(output_directory + "/audio.mp4")

print(videoclip)

new_audioclip = CompositeAudioClip([audioclip])
videoclip.audio = new_audioclip
videoclip.write_videofile("Final.mp4")