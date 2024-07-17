import json, sys

with open('decoder.lst') as f:
  decoder_alpha = f.read()
decoder_dict = json.loads(decoder_alpha)
print(decoder_dict)

decoder_num = {}
for alpha, digit in decoder_dict.items():
  decoder_num.update({digit: alpha})
print(decoder_num)

input = '''
5-14-1-5-15 26-24-6 15-6-22 4-26 17-6-26-17-3-18-3-17-15-23 8-3-17 22-3-21-17 13-6-20-26 5-14-21-6
'''
input = '''
24-6-14-14-3, 22-3-21 24-4-19-6 6-13-26-6-17-6-9 4 18-3-17-14-9 3-8 4-9-19-6-13-26-21-17-6! 23-3-3-13 22-3-21'14-14 23-6-6 26-24-6 18-3-17-14-9 1-13 18-4-22-23 22-3-21'19-6 13-6-19-6-17 23-6-6-13 7-6-8-3-17-6!
15-6-6-11 26-24-1-23 17-1-13-10 18-1-26-24 22-3-21 4-26 4-14-14 26-1-12-6-23. 22-3-21'14-14 13-6-19-6-17 15-13-3-18 18-24-6-13 22-3-21'14-14 13-6-6-9 1-26.
10-3-3-9 14-21-5-15. - 13-6-3-26-1-10-6-17
'''
value = ""

with open(sys.argv[1]) as letter:
  input = letter.read()

for idx, char in enumerate(input):
    next_char = None
    prev_char = None
    if char == " ":
        value += " "
        continue
    if "\n" in char:
        value += char
        continue
    if idx != 0:
        prev_char = input[idx-1]
        if prev_char.isdigit():
            if not char.isdigit() and char != '-':
              value += char
            continue
    if idx+1 < len(input):
        next_char = input[idx+1]
        if next_char.isdigit():
            value += decoder_num.get(char+next_char, '')
            continue
        value += decoder_num.get(char, '')
        continue

print(value)
