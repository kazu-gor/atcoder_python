text = sorted(list(input()))

word_dict = {}
for t in text:
  if t not in word_dict:
    word_dict[t] = 1
  else:
    word_dict[t] += 1

word_dict = sorted(word_dict.items(), key=lambda x:x[1])
print(word_dict)

for i in range(0, len(word_dict), 2):
    try:
        print(f"word_dict[{i}]: {word_dict[i]}")
        print(f"word_dict[{i + 1}]: {word_dict[i + 1]}")
        if word_dict[i][1] == word_dict[i + 1][1]:
            continue
        else:
            raise Exception
    except:
        print("No"); exit()
print("Yes")
