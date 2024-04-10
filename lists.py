articles=['a','b','c','d','e','f','g','h','i']

print(articles[:3])
print(len(articles))
print(articles.index('a'))
print('a' in articles);

for i in range(len(articles)):
    print("1")


squares=[n**2 for n in range(len(articles))]
print(squares)