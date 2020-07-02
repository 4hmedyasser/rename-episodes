import os
import imdb

invalid_characters="~\"#%&*:<>?/\{|}"

ia=imdb.IMDb()

series_id=input("Enter series ID (Number preceeding tt in the IMDb's series URL): ")

series=ia.get_movie(series_id)
ia.update(series, 'episodes')
seasons=sorted(series['episodes'].keys())
episodes=series.data['episodes']

series_path=input("Enter series absolute path (The directory carrying the seasons' directories sorted): ")

series_path=os.path.abspath(series_path)
os.chdir(series_path)

for i in seasons:
    if i<10:
        try:
            season_path=os.path.join(series_path, "0"+str(i))
            os.chdir(season_path)
        except FileNotFoundError:
            break
    else:
        try:
            season_path=os.path.join(series_path, str(i))
            os.chdir(season_path)
        except FileNotFoundError:
            break
    j=1
    for k in sorted(os.listdir()):
        try:
            episode=series['episodes'][i][j]
        except KeyError:
            break
        title=episode['title']
        ext=os.path.splitext(k)[1]
        if i<10:
            if j<10:
                try:
                    os.rename(k, "S0"+str(i)+"E0"+str(j)+"."+title+ext)
                except OSError:
                    print("Inavlid title: "+k+" -> "+"S0"+str(i)+"E0"+str(j)+"."+title+ext)
                    for c in title:
                        if c in invalid_characters:
                            title=title.replace(c, "")
                            os.rename(k, "S0"+str(i)+"E0"+str(j)+"."+title+ext)
                            print("Title modified: "+"S0"+str(i)+"E0"+str(j)+"."+title+ext+"\n")
                        else:
                            pass
            else:
                try:
                    os.rename(k, "S0"+str(i)+"E"+str(j)+"."+title+ext)
                except OSError:
                    print("Inavlid title: "+k+" -> "+"S0"+str(i)+"E"+str(j)+"."+title+ext)
                    for c in title:
                        if c in invalid_characters:
                            title=title.replace(c, "")
                            os.rename(k, "S0"+str(i)+"E"+str(j)+"."+title+ext)
                            print("Title modified: "+"S0"+str(i)+"E"+str(j)+"."+title+ext+"\n")
                        else:
                            pass
        else:
            if j<10:
                try:
                    os.rename(k, "S"+str(i)+"E0"+str(j)+"."+title+ext)
                except OSError:
                    print("Inavlid title: "+k+" -> "+"S"+str(i)+"E0"+str(j)+"."+title+ext)
                    for c in title:
                        if c in invalid_characters:
                            title=title.replace(c, "")
                            os.rename(k, "S"+str(i)+"E0"+str(j)+"."+title+ext)
                            print("Title modified: "+"S"+str(i)+"E0"+str(j)+"."+title+ext+"\n")
                        else:
                            pass
            else:
                try:
                    os.rename(k, "S"+str(i)+"E"+str(j)+"."+title+ext)
                except OSError:
                    print("Inavlid title: "+k+" -> "+"S"+str(i)+"E"+str(j)+"."+title+ext)
                    for c in title:
                        if c in invalid_characters:
                            title=title.replace(c, "")
                            os.rename(k, "S"+str(i)+"E"+str(j)+"."+title+ext)
                            print("Title modified: "+"S"+str(i)+"E"+str(j)+"."+title+ext+"\n")
                        else:
                            pass
        j+=1
print("Done!")
