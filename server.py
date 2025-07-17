import socket
import hamming_distance as H

def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 2209
    server_socket.bind((host, port))
    server_socket.listen(1)
    server_socket.settimeout(40)  # Set your desired timeout value in seconds
    print("Server listening on {}:{}".format(host,port))

    connections = []

    try:
        while True:
            try:
                conn, address = server_socket.accept()
                print("Spelling Request from: ", str(address))
                connections.append(conn)
            except socket.timeout:
                print(f"No Connection received for 40 seconds. Closing server.")
                break

            while True:
                data_as_a_list = []
                try:
                    data = conn.recv(1024).decode('utf-8')
                except socket.timeout:
                    print(f"No data received for 40 seconds. Closing connection.")
                    connections.remove(conn)
                    conn.close()
                    break

                if not data:
                    print('Connection closed by client.')
                    connections.remove(conn)
                    conn.close()
                    break

                if data == '0':
                    print('Closing all connection request.')
                    for connection in connections:
                        connection.close()
                    server_socket.close()
                    break

                print (f"'{str(data)}' was sent from client")
                data_as_a_list = data.split()
                data_result = H.spell_check_in_server(data_as_a_list)
                response = 'NABIH: ' + "\nNABIH: ".join(data_result)
                conn.send(response.encode("utf-8"))

                
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        server_socket.close()        

if __name__ == '__main__':
    server_program()
