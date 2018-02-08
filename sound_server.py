import pyaudio
import socket
from threading import Thread

frames = []

def setvalues():
    FORMAT = pyaudio.paInt16
    CHUNK = 1024
    CHANNELS = 2
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    output = True,
                    frames_per_buffer = CHUNK,
                    )
    return stream, CHUNK, CHANNELS

def udpStream(CHUNK, CHANNELS):

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind((socket.gethostname(), 12345))

    while True:
        soundData, addr = udp.recvfrom(CHUNK * CHANNELS * 2)
        frames.append(soundData)

    udp.close()

def play(stream, CHUNK):
    BUFFER = 10
    while True:
            if len(frames) == BUFFER:
                while True:
                    stream.write(frames.pop(0), CHUNK)

def startstream():
    stream, CHUNK, CHANNELS = setvalues()

    Ts = Thread(target = udpStream, args=(CHUNK, CHANNELS,))
    Tp = Thread(target = play, args=(stream, CHUNK,))
    Ts.setDaemon(True)
    Tp.setDaemon(True)
    Ts.start()
    Tp.start()
    Ts.join()
    Tp.join()


if __name__ == "__main__":
    startstream()
