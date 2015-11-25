with open('movies.txt', 'r') as document:
    dictionary1 = {}
    dictionary2 = {}
    for line in document:
        line = line.strip("\r\n")
        line = line.split(", ")
        dictionary1[line[0]] = line[1:]
    for item in dictionary1:
        movies = item.values()
        print(movies)
        actor = item.keys()
        print(actor)
        for movie in movies:
            if movie not in dictionary2:
                dictionary2.setdefault(movie,[]).append(actor)
            elif movie in dictionary2:
                dictionary2.append(actor)
            else:
                break
