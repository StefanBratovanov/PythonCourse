import itertools

fileName = input()
matchWord = input()

try:
    with open(fileName, encoding='utf-8') as f:
        output = []
        for line in f:
            line = line.rstrip()
            аnagrams = set()

            for permutation in itertools.permutations(line):
                аnagrams.add(''.join(permutation))
            for i in аnagrams:
                if matchWord == i and matchWord != line:
                    # print(line)
                    output.append(line)
        output.sort()
        for i in output:
            print(i)
except Exception as e:
    print("INVALID INPUT")


# words.txt
# horse