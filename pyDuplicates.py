def​ ​find_duplicates​(elements):
    duplicates, seen = set(), set()
​    for​ element ​in​ elements:
​       if​ element ​in​ seen:
        duplicates.add(element)
        seen.add(element)
    ​return​ list(duplicates)


print(find_duplicates(1,2,3,4,5,1,2,7,8,8,7))
