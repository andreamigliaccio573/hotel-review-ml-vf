import random
import pandas as pd

data = []

for i in range(100):
    text = random.choice([
        "camera pulita",
        "camera sporca",
        "check-in veloce",
        "check-in lento",
        "colazione ottima",
        "colazione scarsa"
    ])
    
    dep = random.choice(["Housekeeping", "Reception", "F&B"])
    sent = random.choice(["pos", "neg"])

    data.append({
        "text": text,
        "department": dep,
        "sentiment": sent
    })

df = pd.DataFrame(data)
df.to_csv("../data/reviews_dataset.csv", index=False)

print("Dataset creato!")
