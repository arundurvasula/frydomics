import matplotlib.pyplot as plt
from collections import Counter
import pandas

names = []
with open("README.md", 'r') as f:
    for line in f:
        l = line.split(" ")
        if "[blame" in l:
            names.append(l[l.index('[blame')+1].rstrip().replace("]", "").replace(",", ""))

pandas.Series(Counter(names)).plot(kind='bar')
plt.tight_layout()
plt.savefig("hist.png", dpi=300)
