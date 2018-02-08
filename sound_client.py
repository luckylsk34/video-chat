import pyaudio
import socket
from threading import Thread

frames = []

def setvalues():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = CHUNK,
                    )
    return stream, CHUNK

def udpStream():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        if len(frames) > 0:
            udp.sendto(frames.pop(0), ("10.102.46.36", 12345))

    udp.close()

def record(stream, CHUNK):
    while True:
        frames.append(stream.read(CHUNK))

def startstream():
    stream, CHUNK = setvalues()

    Tr = Thread(target = record, args = (stream, CHUNK,))
    Ts = Thread(target = udpStream)
    Tr.setDaemon(True)
    Ts.setDaemon(True)
    Tr.start()
    Ts.start()
    Tr.join()
    Ts.join()

if __name__ == "__main__":
    startstream()
