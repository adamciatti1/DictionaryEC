
search_values = ['Father', 'God', 'Christ', 'Spirit', 'life', 'man']

#Open file

infile = open('book of John text.txt')
book_john = infile.read()
split_book = book_john.split()

#Make the dictionary

john_dict = {}
for word in split_book:
    if word in john_dict:
        john_dict[word] += 1
    else:
        john_dict[word] = 1

#Display search

for row in search_values:
    for word in john_dict:
        if word == row:
            print(word + ': ' + str(john_dict[word]))