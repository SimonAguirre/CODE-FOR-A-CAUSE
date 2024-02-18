import csv
from anime.models import Animes

# Your CSV data as a string



def run():
    fhand = open('scripts/animetest.csv')
    reader = csv.reader(fhand)
    num = 0
    print(reader.line_num)
    Animes.objects.all().delete()
    for row in reader:
        try:
            # Access the specific column using the index
            title = row[0]
            genres = row[1]
            num_of_ep = row[3]
            img = row[6]
            if(img == ''):
                pass
            elif(num_of_ep == '?'):
                # print(title, genres, num_of_ep, img, "????????")
                pass
            else:
                if(num == 50):
                    break
                try:
                    anime, c = Animes.objects.get_or_create(name=title)
                    # Animes.objects.get_or_create(name=title, genres=genres, num_of_ep=int(num_of_ep), img=img
                    #                     )
                    if c:
                        anime.genres = genres
                        anime.num_of_eps = int(num_of_ep)
                        anime.img = img
                        anime.save()
                        print(title, genres, num_of_ep, img)
                        num += 1
                    
                except Exception as e:
                    print(e)
                    pass
        except:
            pass

    print(num)

run()

                
                
