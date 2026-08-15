def mysplit(strng):
    if string == ""
        return []
    words=[]
    word=""
    for i in string:
          if i.isspace():
              if word != "" :
                  words.append(word)
                  word = ""
          else:
              word+=i
    if word != "":
        words.append(word)

    return words
          

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
    
