import video_server
import sound_server
from threading import Thread

#video_server.startstream()

video = Thread(target = video_server.startstream)
video.start()
sound = Thread(target = sound_server.startstream)
sound.start()
