# Why Chained Comparisons are Better

# Without chaining ( hearder to read ):

score = 85

# You have to write it like this
if score > 50 and score < 100:
    print("Valid score")


# With chaining ( cleaner and more readable ):
score = 85

# Much more elegant
if 50 < score < 100:
    print("Valid score")