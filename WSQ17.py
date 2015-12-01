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
print(("The Movie Titles available are: ")+str(dictionary.keys()))
movie1 = input("Choose a title: ")
movie2 = input("Choose another title: ")
print (("The actors that participated on those move titles were: ")+ str(dictionary.get(movie1))+ str(dictionary.get(movie2)))
answer = []
for a in dictionary.get(movie1):
    for b in dictionary.get(movie2):
        if a == b:
            answer.append(a)
print (("The actors that appear in both movies are: ")+str(answer))
