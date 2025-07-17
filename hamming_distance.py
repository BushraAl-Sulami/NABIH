import multiprocessing
import pyarabic.araby as araby   
import jellyfish as fish

def spell_check(word, dict):
    # Check if the word is valid Arabic
    if not araby.is_arabicrange(word):
        return
    # Generate a list of similar words based on edit distance
    similar_words = [w for w in dict if  fish.hamming_distance(word, w) <= 1 & fish.hamming_distance(word, w) != 0 ]
    return similar_words


try:
    with open(r"Arab_Eyes_Technical_Dictionary.txt", 'r', encoding="utf-8") as file:
        dictionary = file.read().split()
except (FileNotFoundError, PermissionError) as e:
    print("Error opening the dictionary file:", str(e))


def spell_check_in_server(data):
    # create a pool of workers with 4 processes
    pool = multiprocessing.Pool(4)
    # use map to apply the spell_check function to each token in parallel
    # and get a list of results
    results = pool.starmap(spell_check, [(word, dictionary) for word in data])
    # close and join the pool
    pool.close()
    pool.join()
    list_of_responses = []
    for word, suggestions in zip(data, results):
        if suggestions:
           list_of_responses.append(f"Spelling mistake: {word} || Suggestions:{suggestions}")
        else:
            list_of_responses.append(f"No Spelling Mistakes Detected in {word}")    
    return list_of_responses

