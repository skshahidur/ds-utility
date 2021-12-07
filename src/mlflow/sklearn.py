from sklearn.metrics import classification_report
import numpy as np

labels = list("abcd")

for i in range(50):
    print(np.random.choice(labels))