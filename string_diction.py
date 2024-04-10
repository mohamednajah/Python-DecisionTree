# zipcode="1234x"


# def is_valid_zipcode(zipcode):
#     if(zipcode.isdigit() and len(zipcode)==5):
#         return "good"
#     else:
#         return "bad"

# print(is_valid_zipcode(zipcode))       

################# WORD RESEARCH FOR A SPECIFIC WORD #################
doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
def word_search(doc_list, keyword):
 indexs=[]
 for i,doc in enumerate(doc_list):
        tokens=doc.split()
    
        normalized=[token.rstrip('.,').lower() for token in tokens]
        if(keyword.lower() in normalized):
            indexs.append(i)
            
 return indexs 

print(word_search(doc_list,"casino"))

################# MULTI KEYWORD RESEARCH FOR A SPECIFIC WORD #################

def multiplewords_research(doc_list,keywords):
    list={}
    for keyword in keywords:
        list[keyword]=word_search(doc_list,keyword)
    return list


keywords=["casino", "they"]

print(multiplewords_research(doc_list,keywords))



