import numpy as np
import matplotlib.pyplot as plt
import const as _c

y1, y2 = _c.POS[:, 0], _c.POS[:, 1]
text = range(1, 25)
plt.figure()
plt.xlim(0, 30.1)
plt.ylim(0, 29.8)

plt.scatter(y1, y2, marker='.', s=10, c='b')
for i in range(24):
    plt.text(y1[i]+0.3, y2[i]+0.3, str(text[i]))
plt.show()
