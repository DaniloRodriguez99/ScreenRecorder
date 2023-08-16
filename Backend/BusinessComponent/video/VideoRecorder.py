import time
import wave
import threading  # <-- Import threading
from datetime import datetime
from typing import Optional

import cv2
import numpy
import pyaudio
import pyautogui
from flask_socketio import SocketIO
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip

from BusinessComponent.video.IVideoRecorder import IVideoRecorder
from Models.RecordSettings import RecordSettings


class VideoRecord(IVideoRecorder):

    def __init__(self, socket: SocketIO, settings: Optional[RecordSettings] = RecordSettings(),
                 fileName: Optional[str] = "output_video"):
        self.recordSettings = settings
        self.fourcc = cv2.VideoWriter_fourcc(*self.recordSettings.video_format)  # formato de video
        self.screen_size = (self.recordSettings.screen_weight, self.recordSettings.screen_height)
        self.output_file = fileName + ".avi"
        self.audio_output_file = fileName + ".wav"
        self.audio_frames = []
        self.isRecording: bool = False
        self.socket = socket
        self.wasStopped = False

    def record_checker(self, video_thread, audio_thread):
        print("Chequeando")
        video_thread.join()
        audio_thread.join()
        print("Terminaron de grabar")
        self.isRecording = False
        self.socket.emit('record_end', True )
        self.combine_audio_video()

    def Record(self, settings: RecordSettings):
        # Start the threads using threading.Thread
        self.PrintVideoData()
        video_thread = threading.Thread(target=self.record_video)
        audio_thread = threading.Thread(target=self.record_audio)
        record_checker_thread = threading.Thread(target=self.record_checker, args=(video_thread, audio_thread))
        video_thread.start()
        audio_thread.start()

        self.isRecording = True
        record_checker_thread.start()

    def IsRecording(self) -> bool:
        return self.isRecording

    def record_video(self):
        print("Comienza a capturar pantalla")
        start_time = time.time()
        videoFrames = []
        try:
            while (time.time() - start_time < self.recordSettings.duration) and (self.wasStopped == False):
                # Captura de pantalla
                screenshot = pyautogui.screenshot()
                frame = cv2.cvtColor(numpy.array(screenshot), cv2.COLOR_RGB2BGR)
                videoFrames.append(frame)

        except KeyboardInterrupt:
            print("Error en captura de video")
            pass

        fps = len(videoFrames) / (time.time() - start_time)
        print("Numeros de imagenes conseguidas:", len(videoFrames))
        print("Numero de segundos capturados:", round(time.time() - start_time))
        print("Los fps que se alcanzaron fueron:", fps)
        out = cv2.VideoWriter(self.output_file, self.fourcc, fps, self.screen_size)
        for frame in videoFrames:
            out.write(frame)

        out.release()
        cv2.destroyAllWindows()
        pass

    def record_audio(self):
        print("Recording audio...")
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100

        p = pyaudio.PyAudio()
        input_device_index = 2

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        input_device_index=input_device_index,
                        frames_per_buffer=CHUNK)

        for _ in range(int(RATE / CHUNK * self.recordSettings.duration)):
            data = stream.read(CHUNK)
            self.audio_frames.append(data)
            if self.wasStopped:
                print("Grabación de audio detenida")
                break

        stream.stop_stream()
        stream.close()

        p.terminate()

        wf = wave.open(self.audio_output_file, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(self.audio_frames))
        wf.close()


    def SetRecordSetting(self, recordSettings: RecordSettings):
        self.recordSettings = recordSettings

    def combine_audio_video(self):
        self.wasStopped = False;
        print("Combinando audio y video....")
        video_clip = VideoFileClip(self.output_file)
        audio_clip = AudioFileClip(self.audio_output_file)

        min_duration = min(video_clip.duration, audio_clip.duration)
        video_clip = video_clip.subclip(0, min_duration)
        audio_clip = audio_clip.subclip(0, min_duration)

        final_video_clip = CompositeVideoClip([video_clip.set_audio(audio_clip)])

        date_format = "%Y-%m-%d %H:%M:%S"
        fecha_actual = datetime.now()
        fecha_actual_str = fecha_actual.strftime(date_format) + ".mp4"
        fecha_actual_str = fecha_actual_str.replace(" ", "_")
        fecha_actual_str = fecha_actual_str.replace(":", "_")

        final_video_clip.write_videofile(self.recordSettings.directory + "/" + fecha_actual_str, codec="libx264", threads=6)
        print("Combinado")

    def GetRecordSetting(self):
        return self.recordSettings
    def PrintVideoData(self):
        print("Detalles de configuracion del video")
        print("Duracion: " + str(self.recordSettings.duration))
        print("Cuadros por segundo: " + str(self.recordSettings.fps))
        print("Tamaño de pantalla: " + str(self.recordSettings.screen_weight) + "x" + str(self.recordSettings.screen_height))
        print("Formato del video: " + self.recordSettings.video_format)
        print("Nombre del archivo: " + self.output_file)
        print("Ruta de guardado: " + str(self.recordSettings.directory))

    def StopRecording(self):
        self.wasStopped = True
        return self.wasStopped

