import collections

with open('wakati_list.txt', 'r', encoding='utf-8') as f:
    list = f.read().replace('\n', ' ').split(' ')
    print(len(list))
    
    counts = collections.Counter(list).items()
    sourted_counts = sorted(counts, key=lambda t:t[1], reverse=True)
    sourted_counts = sourted_counts[:100]

    for k, v in sourted_counts:
        print(k, v, sep=':')