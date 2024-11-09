def single_root_words(root_word,*other_words):

    same_words = []

    for i in other_words[:] :

        root_word = root_word.lower()  # Перевел все значения в нижний регистр, чтобы избежать его влияния при сравнении строк.
        i = i.lower()                  # В итоге значения во втором списке выводятся в нижнем регистре. Это критично?

        if root_word in i or i in root_word:
            same_words.append(i)

    print(same_words)





single_root_words('rich','richest','orichalcum','cheers','richies')
single_root_words('Disablement','Able','Mable','Disable','Bagel')


