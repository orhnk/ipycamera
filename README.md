# **`IPYCamera`**

This project implements a video streaming client in Python.

## Overview

The client connects to a video stream, captures JPEG frames in buffers, extracts
full frames, decodes them using OpenCV and displays the video.

## Usage

Run the client:

```sh
python camera.py <HOST>
```

Where `<HOST>` is the IP and port of the video stream server.

Press ESC to stop the video.

## How it works

- Connect to video stream URL with urllib
- Read 1024 byte buffers from stream
- Append each buffer to a list
- Check buffers for JPEG start/end markers
- Extract full JPEG frames from buffers
- Decode JPEGs with OpenCV
- Display video frames

Buffering is needed because a JPEG frame may span multiple chunks from the
stream.

## Contributing

Contributions welcome! Please open an issue or PR.

## License

This project is licensed under the MIT License. See LICENSE for details.
