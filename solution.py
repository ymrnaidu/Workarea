from socket import *
import base64
import time

def smtp_client(port, mailserver):
    msg = "\r\n Madhu's SMTP homework"
    endmsg = "\r\n.\r\n"

    # Fill in start
    mymailserver = (mailserver, port)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mymailserver)
    # Fill in end
    
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    if recv[:3] != '220':
         print('220 reply not received from server.')

    # Send HELO command and print server response.         
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFrom = "MAIL FROM:<ymrnaidu@yahoo.com>\r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptTo = "RCPT TO:<ymrnaidu@yahoo.com> \r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = "DATA\r\n\r\n" 
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print("DATA details: " + recv4)
    # Fill in end

    # Send message data.
    # Fill in start
    subject = "Subject: NYU Semister 1 SMTP mail client testing \r\n" 
    clientSocket.send(subject.encode())
    mailmsg = "Input here message: \r\n"
    clientSocket.send(mailmsg.encode())
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024).decode()
    #print(recv_msg)
    # Fill in end
    
    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    clientSocket.send("QUIT\r\n".encode())
    message=clientSocket.recv(1024)
    #print (message)
    clientSocket.close()
    # Fill in end
    
    
if __name__ == '__main__':
    smtp_client(25, 'smtp.nyu.edu')

