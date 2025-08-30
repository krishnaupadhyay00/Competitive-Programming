# * * * * *
# - * * * *
# -- * * *
# --- * *
# ---- *

n=int(input())
for i in range(n):
    print("-" * i, end=" ")
    for j in range(n - i):
        print("*", end=" ")
    print()

