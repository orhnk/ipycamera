import cv2
from urllib.request import urlopen
import numpy as np
import sys

host = "192.168.1.4:8080"
if len(sys.argv) > 1:
    host = sys.argv[1]

hoststr = "http://" + host + "/video"
print("Streaming " + hoststr)

stream = urlopen(hoststr)

# Initialize a buffer to store bytes
bytes_buffer = b""

while True:
    bytes_buffer += stream.read(1024)

    # Print length of buffer for debugging
    print("Buffer length:", len(bytes_buffer))

    a = bytes_buffer.find(b"\xff\xd8")
    b = bytes_buffer.find(b"\xff\xd9")
    if a != -1 and b != -1:
        print("Found JPEG start/end markers")

        jpg = bytes_buffer[a : b + 2]

        # Print JPEG length
        print("JPEG length:", len(jpg))

        bytes_buffer = bytes_buffer[b + 2 :]

        try:
            i = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
        except cv2.error as e:
            print("Error decoding JPEG frame:", e)
            continue

        cv2.imshow(hoststr, i)
        if cv2.waitKey(1) == 27:
            break

cv2.destroyAllWindows()
