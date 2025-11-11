from collections import Counter

text = "Harvard uses the title President"\
        "rather than"\
        "Vice-Chancellor "\
        "which is more common in British and Commonwealth universities."\
        "Would you like me to tell you a bit about Henry Dunsters" \
        "background and contributions to Harvard?"

words = text.split()

counter = Counter(words)
print(counter)
top_three = counter.most_common(3)
print(top_three)



