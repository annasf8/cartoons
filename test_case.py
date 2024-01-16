
def generate_movie_script():
    prompt = input('Enter your theme: ', default="ecology"or "cosmos" or "medicine" or "peace")
    universe = [
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

         ]
    location = input(choices="beautiful valley meadow with clover flowers" or "a cold dungeon with bats, resembling an abandoned mine" or "azure ocean with tropical fish and corals")
    emotions = input(choices="irritation" or "anger" or "surprise" or "joy" or "competitive" or "spirit" or "pride" or "fatigue")
    res = prompt + universe + location + emotions
    return res

print(generate_movie_script)