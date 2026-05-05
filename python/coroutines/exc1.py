# -------------------------
# title: History Keeper
# -------------------------
# -------------------------
# Description:
# Create a generator
# and use send.
# -------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander Volkovich.
# AI2 InfinityLabs.
# ------------------------------
def history_keeper(length: int):
    ls = []
    while True:
        num = yield ls
        if len(ls) < length:
            ls.append(num)
        else:
            ls.pop(0)
            ls.append(num)


history_length = 3
num_elements = 4
hk = history_keeper(history_length)
ls = []
history = hk.send(None)
print(history)
for i in range(1, num_elements):
    history = (hk.send(i))
    print(history)


