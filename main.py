import re

#inp = input("Cryptogram word : ")
inp="that"
with open("eng10k.txt", "r") as f:
  testWords = f.readlines()

for w in range(len(testWords)):
  testWords[w] = testWords[w][0:-1]

def letter_of(word):
	out = []
	for l in word:
		if not (l in out):
			out.append(l)


def make_nl(l):
	out = ""
	for i in range(l):
		out += "\\" + str(i + 1)
	if not (l == 0):
		out = "(?!" + out + ")"
	return out


def make_reg(word, exclude_self):
	used_letters = []
	out = "^"
	for l in word:
		if l in used_letters:
			out = out + "\\{}".format(used_letters.index(l) + 1)
		else:
			if exclude_self:
				out = out + "({}[^{}])".format(make_nl(len(used_letters)), l)
			else:
				out = out + "({}.)".format(make_nl(len(used_letters)))
			used_letters.append(l)

	return out + "$"


def match_list(r, l):
	out = []
	for w in l:
		if re.match(r, w):
			out.append(w)
	return out


def filter_reg(r, l, exclude_self=True):
	return match_list(make_reg(r.lower(), exclude_self), l)


print(make_reg(inp.lower(), False))
print(filter_reg(inp, testWords, True))
