def acronym(phrase):
    phraselist = phrase.split()

    answer = ""
    for word in phraselist:
        answer += word[0]
    return answer

print(acronym(input("Enter words for acronym: ")))
