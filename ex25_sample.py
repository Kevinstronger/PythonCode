import ex25

sentence = "All good things come to those who wait"
words = ex25.break_words(sentence)
print words

print "-"*30
sorted_words = ex25.sort_words(words)
print sorted_words

print "-"*30
print ex25.print_first_word(words)
print ex25.print_last_word(words)

print "-"*30
print ex25.print_first_word(sorted_words)
print ex25.print_last_word(sorted_words)

print "-"*30
sorted_words2 = ex25.sort_sentence(sentence)
print sorted_words2


print "-"*30
print ex25.print_first_and_last(sentence)


print "-"*30
print ex25.print_first_and_last_sorted(sentence)

'''
Result:
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait']
------------------------------
['All', 'come', 'good', 'things', 'those', 'to', 'wait', 'who']
------------------------------
All
None
wait
None
------------------------------
All
None
who
None
------------------------------
['All', 'come', 'good', 'things', 'those', 'to', 'wait', 'who']
------------------------------
All
wait
None
------------------------------
All
None
'''