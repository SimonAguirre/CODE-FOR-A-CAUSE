from django.contrib.auth.models import User
from anime.models import Anime, Animes
import random

anime_reviews = [
    "I absolutely loved this anime! The character development was top-notch, and the plot twists kept me on the edge of my seat.",
    "A masterpiece! The animation quality is stunning, and the emotional depth of the story is truly captivating.",
    "This anime is a rollercoaster of emotions. I laughed, cried, and couldn't get enough of the intense action scenes.",
    "A must-watch for any anime fan. The world-building is incredible, and the soundtrack is simply amazing.",
    "I was skeptical at first, but this anime completely exceeded my expectations. The writing is brilliant, and the voice acting is superb.",
    "The character designs are unique, and the humor in this anime is spot-on. It's a perfect blend of comedy and drama.",
    "I binged-watched this anime in one sitting! The pacing is perfect, and each episode leaves you wanting more.",
    "The themes explored in this anime are thought-provoking, and the moral dilemmas faced by the characters add a layer of complexity to the story.",
    "I've watched a lot of anime, and this one stands out. The world is richly detailed, and the lore is fascinating.",
    "If you're a fan of suspense and mystery, this anime is for you. The plot twists are mind-bending, and you'll be guessing until the very end.",
    "An anime that pulls at the heartstrings! The emotional journey of the characters is beautifully portrayed, and the soundtrack enhances every moment.",
    "This anime is a visual feast. The art style is unique, and the attention to detail in the animation is commendable.",
    "A hidden gem! The story is engaging, and the supporting characters are just as compelling as the main ones.",
    "I couldn't stop smiling throughout this anime. It's a feel-good series with a perfect blend of humor and heartwarming moments.",
    "The world-building in this anime is out of this world. The lore is vast, and every episode uncovers new layers of the fascinating universe.",
    "This anime left me in awe. The fight scenes are incredibly well-choreographed, and the power scaling is on point.",
    "A perfect mix of science fiction and fantasy! The plot is intriguing, and the futuristic elements are seamlessly integrated into the narrative.",
    "The character relationships in this anime are beautifully explored. It's not just about the action; it's about the bonds formed along the way.",
    "If you're a fan of psychological thrillers, look no further. The mind games played by the characters will keep you guessing until the end.",
    "This anime is a visual and auditory treat. The sound design is phenomenal, and the opening theme is now stuck in my head.",
    "A thought-provoking storyline that delves into existential questions. It's intellectually stimulating and emotionally resonant.",
    "The comedic timing in this anime is impeccable. I found myself laughing out loud in every episode.",
    "An underrated masterpiece! The character arcs are well-developed, and the narrative keeps you invested from start to finish.",
    "I marathoned this anime, and it was a wild ride. The plot twists are jaw-dropping, and the cliffhangers are relentless.",
    "This anime redefines the isekai genre. The protagonist's journey feels fresh, and the world they inhabit is full of surprises.",
    "A tearjerker that explores the fragility of life. Be prepared for an emotional rollercoaster that will stay with you long after it's over.",
    "The animation quality in this anime is consistently high. The attention to detail in every frame is a testament to the dedication of the animators.",
    "An anime with a strong social commentary. It tackles relevant issues while still delivering an entertaining and gripping narrative.",
    "The world of this anime is so immersive that I wish I could live in it. The creativity in the world design is simply astounding.",
    "I haven't been this emotionally invested in an anime in years. The character arcs are beautifully crafted, and the ending is satisfying.",

]

status_choice = ['Watching', 'Finished', 'Plan to Watch']

animes = list(Animes.objects.all())

def run():
    Anime.objects.all().delete()
    users = User.objects.all()[1:]
    for user in users:
        for i in range(random.randint(15,20)):
            rating = random.randint(0,10)
            favorite = random.choice([True, False])
            comment = random.choice(anime_reviews)
            current_ep = random.randint(0,12)
            owner = user
            status = random.choice(status_choice)
            anime = random.choice(animes)
            Anime.objects.create(anime=anime, rating=rating, favorite=favorite, comment=comment, current_episode=current_ep, owner=owner, status=status)
