import video_client
import sound_client
from threading import Thread

#video_client.startstream()

video = Thread(target = video_client.startstream)
video.start()
sound = Thread(target = sound_client.startstream)
sound.start()
