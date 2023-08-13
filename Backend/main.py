import threading

import eventlet
from flask import Flask
from flask_socketio import SocketIO, emit

from BusinessComponent.controller import MainController
from BusinessComponent.video.IVideoRecorder import IVideoRecorder
from BusinessComponent.video.VideoRecorder import VideoRecord
from DataAccess.SqlLiteDA import SqlLiteDA
from Models.RecordSettings import RecordSettings

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
controller: MainController = MainController(dataAccess=SqlLiteDA())
videoRecorder: IVideoRecorder = VideoRecord(fileName="Prueba1", socket=socketio)


@socketio.on('record_start')
def handleStartRecord(recordsettings_json):
    global videoRecorder  # Ensure we are working on the global instance
    print("SOCKET - Start Record")
    recordSettings = RecordSettings.from_json(recordsettings_json)
    videoRecorder = VideoRecord(settings=recordSettings, fileName="Prueba1", socket=socketio)
    threading.Thread(target=videoRecorder.Record).start()
    print("Terminando record_start")
    emit("record_start", True, broadcast=True)


@socketio.on('record_cancel')
def handleCancelRecord():
    global videoRecorder  # Ensure we are working on the global instance
    print("SOCKET - Cancel Record")
    videoRecorder.StopRecording()
    print("Enviando datos")
    emit("record_cancel", True, broadcast=True)


@socketio.on('getRecordSettings')
def handleGetConfiguration():
    print("SOCKET - getRecordSettings")
    recordSettings = controller.GetSettings()
    json_result = recordSettings.to_json()
    emit("getRecordSettings", json_result, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
