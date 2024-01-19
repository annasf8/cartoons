import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
# print(os.environ.get("OPENAI_API_KEY"))
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {
      "role": "user",
      "content": "Write a Python function that takes variables: prompt, heroes, location, emotions, prologue from this file and create a cartoon with style like in National Geographic Channel."
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
def generate_movie_script():
    prompt = input('Enter your theme: ', default="ecology"or "cosmos" or "medicine" or "peace")
    heroes = [
        {'Watery': {"gender": "girl",
                  "instance": "drop of water",
                    "eyes": "deep blue",
                    "hairs": "long blue and grey",
                    "character": "dreamy and charming"}},
         {'Flame': {"gender": "boy",
                    "instance": "fire",
                    "eyes": "orange",
                    "hairs": "ginger",
                    "character": "explosive and sly"}},
        {'Bougnat': {"gender": "afro-boy",
                   "instance": "ember",
                   "eyes": "black",
                   "hairs": "curly",
                   "character": "strong and wary"}},
        {'Brieze': {"gender": "asian girl",
                     "instance": "wind",
                     "eyes": "brown",
                     "hairs": "long black",
                     "character": "attractive and windy"}},
        {'Leafy': {"gender": "boy",
                    "instance": "a leaf from oak tree",
                    "eyes": "green",
                    "hairs": "can make different colors",
                    "character": "clever and kind"}},

         ]
    location = input(choices="beautiful valley meadow with clover flowers" or "a cold dungeon with bats, resembling an abandoned mine" or "azure ocean with tropical fish and corals")
    emotions = input(choices="irritation" or "anger" or "surprise" or "joy" or "competitive" or "spirit" or "pride" or "fatigue")
    universe = prompt + heroes + location + emotions
    return universe


prologue = "The world is not at all what it seems at first." \
           "Every day our heroes learn something new about the world they live in. " \
           "But they are unusual inhabitants of it, just because there are the instances," \
           " from whom our world was created. Here there are: ember, water, air, fire and life." \
           " Join their search and debates and make a lot of discoveries for yourself. Let's start!"

epizode_example = "Different letters." \
            " Bougnat: "Look what I've dug up. An antique spoon. ' \
                                   "And there's an engraving on it. Can't read."
            'Flame: Let me light it up. It's a silver.The letters "B" and "C"."
            'Brieze: 'I think it was belonged to some Brieze Cooper from the past, here are initials like mine.'
            'Watery': "Let me look in my transparent mirror into the past. " \
                      "It belonged to the girl, named Vera Sokol from the family of pre-revolutionary russian emigrants."
            'Brieze: "And what's the link with letters?
            'Leafy': 'The world is not at all what it seems at first. It's russian letters, the first letters of her firstname and surname'!"

