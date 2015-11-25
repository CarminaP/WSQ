with open('movies.txt', 'r') as document:
    movie_dict = {}
    for line in document:
        line = line.strip("\r\n")
        line = line.split(", ")
        for i in range(0,(len(line)-1)):
            if line[i+1] not in movie_dict:
                movie_dict[line[i+1]] = line[0]
            elif line[i+1] in movie_dict:
                key = line[i+1]
                movie_dict.setdefault(key, [])
                movie_dict[key].append(line[0])
        print (movie_dict)
