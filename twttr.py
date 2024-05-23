tweet = input("Input: ").strip()
for char in tweet:
    if char in ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']:
        tweet = tweet.replace(char, "", 1)
print("Output:", tweet)