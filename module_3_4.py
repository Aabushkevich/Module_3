def single_root_words(root_word,*other_words):

    same_words = []

    for i in other_words[:] :

        if root_word.lower() in str(i.lower()) or str(i.lower()) in root_word.lower():
            same_words.append(i)

    print(same_words)





single_root_words('rich','richest','orichalcum','cheers','richies')
single_root_words('Disablement','Able','Mable','Disable','Bagel')


