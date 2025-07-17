import pyarabic.araby as araby
import time

def optimal_string_alignment_distance(s1, s2):
    # Create a table to store the results of subproblems
    dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
     
    # Initialize the table
    for i in range(len(s1)+1):
        dp[i][0] = i
    for j in range(len(s2)+1):
        dp[0][j] = j
 
    # Populate the table using dynamic programming
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
 
    # Return the edit distance
    return dp[len(s1)][len(s2)]



with open(r"gamers1.txt", 'r', encoding="utf-8") as file:
    text = file.read().split()
    tokens = []
    for txt in text :
        tokens += araby.tokenize(txt)

with open(r"Arab_Eyes_Technical_Dictionary.txt", 'r', encoding="utf-8") as file:    
    words = file.read().split() 


def spell_check(token, words):
    # Check if the word is valid Arabic
    if not araby.is_arabicrange(token):
        return 
    # Generate a list of similar words based on edit distance
    similar_words = [w for w in words if optimal_string_alignment_distance(token, w) <= 1 & optimal_string_alignment_distance(token, w) != 0 ]
    return similar_words


start = time.perf_counter()
for token in tokens:
    suggestions = spell_check(token, words)
    if suggestions:
        print(f"Spelling mistake: {token}. Suggestions: {suggestions}")
print("time taken is: ",time.perf_counter() - start )


