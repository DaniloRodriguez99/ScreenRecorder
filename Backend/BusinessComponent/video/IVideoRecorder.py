from abc import ABC, abstractmethod

from Models.RecordSettings import RecordSettings


class IVideoRecorder(ABC):

     @abstractmethod
     def Record(self):
         pass

     @abstractmethod
     def GetRecordSetting(self):
         pass

     @abstractmethod
     def SetRecordSetting(self, setting: RecordSettings):
         pass

     @abstractmethod
     def PrintVideoData(self):
         pass


     @abstractmethod
     def IsRecording(self)->bool:
         pass


     @abstractmethod
     def StopRecording(self):
         pass