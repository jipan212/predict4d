import random


def generate_prediction(pos_freq,total=10):

    d1=[x[0] for x in pos_freq[0].most_common(5)]
    d2=[x[0] for x in pos_freq[1].most_common(5)]
    d3=[x[0] for x in pos_freq[2].most_common(5)]
    d4=[x[0] for x in pos_freq[3].most_common(5)]

    preds=[]

    for i in range(total):

        num=(
        random.choice(d1)
        +random.choice(d2)
        +random.choice(d3)
        +random.choice(d4)
        )

        preds.append(num)

    return list(set(preds))