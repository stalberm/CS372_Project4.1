import socket
import datetime

host = "time.nist.gov"
port = 37

def system_seconds_since_1900():
    """
    The time server returns the number of seconds since 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(datetime.datetime.now().strftime("%s"))
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1900_epoch

sock = socket.socket()
sock.connect((host, port))

data = sock.recv(4)
sock.close()

nist = int.from_bytes(data, "big")
system = system_seconds_since_1900()

print("NIST time:", nist)
print("System time:", system)

