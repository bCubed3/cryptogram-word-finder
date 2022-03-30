import re

inp = "abccad"
testWords = ["little", "tweets", "hello", "abccad", "xxxxxx", "littles", "belittle"]


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


def make_reg(word):
    used_letters = []
    out = "^"
    for l in word:
        if l in used_letters:
            out = out + "\\{}".format(used_letters.index(l) + 1)
        else:
            out = out + "({}[^{}])".format(make_nl(len(used_letters)), l)
            used_letters.append(l)

    return out + "$"


def match_list(r, l):
    out = []
    for w in l:
        if re.match(r, w):
            out.append(w)
    return out


def filter_reg(r, l):
    return match_list(make_reg(r.lower()), l)


print(make_reg(inp.lower()))
print(filter_reg(inp, testWords))
