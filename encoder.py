import json,sys

with open('decoder.lst') as f:
  decoder_alpha = f.read()
decoder_dict = json.loads(decoder_alpha)
print(decoder_dict)

decoder_num = {}
for alpha, digit in decoder_dict.items():
  decoder_num.update({digit: alpha})
print(decoder_num)

input = '''
HELLO CHILD, YOU HAVE ENTERED A WORLD OF ADVENTURE! SOON YOU'LL SEE THE WORLD IN WAYS YOU'VE NEVER SEEN BEFORE!
KEEP THIS RING WITH YOU AT ALL TIMES. YOU'LL NEVER KNOW WHEN YOU'LL NEED IT.
GOOD LUCK. - NEOTIGER
'''

with open(sys.argv[1]) as letter:
  input = letter.read().upper()

value = ""
length = len(input)
for idx, char in enumerate(input):
    if char == " ":
        value += " "
        continue
    if not char.isalpha():
        value += char
        continue
    value += decoder_dict[char]
    if idx+1 < length:
      if input[idx+1].isalpha():
        value += "-"
print(value)
