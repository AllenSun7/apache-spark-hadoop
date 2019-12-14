dic_anagram = {"fdsd": 6,
                "fdasfd": 5}
list_anagram = []

for key, value in dic_anagram.items():
    word_dic = {key: value}
    list_anagram.append(word_dic)
print(list_anagram)

list_anagram2 = [{key: value} for key, value in dic_anagram.items()]
print(list_anagram)