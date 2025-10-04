def count_words(word):
    no_words = word.split()
    print (f"Found {len(no_words)} total words")

    
def count_character(input_text):
    stat_dic = {}
    formatted_text = input_text.lower()
    #print(formatted_text)

    for i in range (0,len(formatted_text)):
        stat_dic.setdefault(formatted_text[i],0)
        #print(formatted_text[i])
        stat_dic[formatted_text[i]] += 1
    #print(stat_dic)
    return stat_dic

def sort_on(items):
    return items["num"]

def sorting_dictionaries(dic):
    #print(dic)
    temp_list = []
    for key in dic:
        if key.isalpha():
            temp_list.append({"char":key, "num":dic[key]})
            #print(temp_list)
    #print(temp_list)
    temp_list.sort(reverse=True, key=sort_on)
    return(temp_list)
    #print(temp_list)
    #print(sorted_list)

def clean_print(list):
    for i in range (0,len(list)):
        print(f"{list[i]["char"]}: {list[i]["num"]}")

