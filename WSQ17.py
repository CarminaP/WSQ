with open('movies.txt', 'r') as document:
    dictionary = {}
    for line in document:
        line = line.strip("\r\n")
        line = line.split(", ")
        for i in range (1, (len(line)-1)):
            movie = line[i]
            actor = line[0]
            if movie not in dictionary:
                dictionary[movie] = [actor]
            else:
                dictionary[movie].append(actor)
