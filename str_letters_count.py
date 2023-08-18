def make_dict(x):
    dic= {}
    for letter in x:
        dic[letter] = 1 + dic.get(letter, 0)
    return dic


def most_frequent():
    str=input("Input:Please enter a string   \n")
    letters = [letter.lower() for letter in str if letter.isalpha()]
    dic = make_dict(letters)
    result = []
    for key in dic:
        result.append((dic[key], key))
    result.sort(reverse=True)
    print("Output: ")
    for count, letter in result:
        print("{}={}".format(letter, count))
    
