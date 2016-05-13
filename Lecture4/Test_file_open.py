import logging

logging.basicConfig(filename='task2.log', level=logging.DEBUG)
logging.debug("   ")
logging.warning(" асаса")

f = open("catalog_sample.csv")
for idx, line in enumerate(f):
    print(idx + 1, ": ", line.rstrip())
f.close()

for line in f:
    print(line)
f.close()

# very important :) work with files
with open(...) as f:
    for idx, line in enumerate(f):
        print(idx + 1, ": ", line.rstrip())
