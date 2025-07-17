import pyarabic.araby as araby
import time
import socket 
def editDistance(str1, str2):
	# Get the lengths of the input strings
	m = len(str1)
	n = len(str2)
	
	# Initialize a list to store the current row
	curr = [0] * (n + 1)
	
	# Initialize the first row with values from 0 to n
	for j in range(n + 1):
		curr[j] = j
	
	# Initialize a variable to store the previous value
	previous = 0
	
	# Loop through the rows of the dynamic programming matrix
	for i in range(1, m + 1):
		# Store the current value at the beginning of the row
		previous = curr[0]
		curr[0] = i
		
		# Loop through the columns of the dynamic programming matrix
		for j in range(1, n + 1):
			# Store the current value in a temporary variable
			temp = curr[j]
			
			# Check if the characters at the current positions in str1 and str2 are the same
			if str1[i - 1] == str2[j - 1]:
				curr[j] = previous
			else:
				# Update the current cell with the minimum of the three adjacent cells
				curr[j] = 1 + min(previous, curr[j - 1], curr[j])
			
			# Update the previous variable with the temporary value
			previous = temp
	
	# The value in the last cell represents the minimum number of operations
	return curr[n]

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
    similar_words = [w for w in words if editDistance(token, w) <= 1 & editDistance(token, w) != 0 ]
    return similar_words

server_address = ('localhost', 4000)  # Use the same address and port as the client
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
   
   
    server_socket.bind(server_address)
    server_socket.listen()

    print(f"Server listening on {server_address}")

    # Wait for a connection
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()

    try:
        print(f"Connection from {client_address}")

        # Receive tokens from the client
        received_tokens = []
        while True:
            data = connection.recv(1024).decode('utf-8')
            if data == "bye":
                break  # Exit the loop when the word "Bey" is received
            received_tokens.append(data)

        # Perform spell check on received tokens
        errors = []
        for token in received_tokens:
            suggestions = spell_check(token, words)
            if suggestions:
                errors.append(f"Spelling mistake: {token}. Suggestions: {suggestions}")

        # Send errors back to the client
        response = '\n'.join(errors)
        connection.sendall(response.encode('utf-8'))

    finally:
        # Clean up the connection
        connection.close()

start = time.perf_counter()
for token in tokens:
    suggestions = spell_check(token, words)
    if suggestions:
        print(f"Spelling mistake: {token}. Suggestions: {suggestions}")
print("time taken is: ",time.perf_counter() - start )