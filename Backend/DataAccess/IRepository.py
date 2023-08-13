from abc import ABC, abstractmethod

from Models.RecordSettings import RecordSettings
from Models.ScheduleRecord import ScheduleRecordModel


class IRepository(ABC):

    @abstractmethod
    def SaveConfiguration(self, settings: RecordSettings):
        pass

    @abstractmethod
    def CreateConfiguration(self, settings: RecordSettings):
        pass
    @abstractmethod
    def GetSettings(self):
        pass

    @abstractmethod
    def ScheduleRecord(self, scheduledRecord: ScheduleRecordModel):
        pass

    @abstractmethod
    def CancelScheduledRecord(self, scheduledRecord: ScheduleRecordModel):
        pass

    @abstractmethod
    def GetMyScheduledRecords(self):
        pass

    @abstractmethod
    def SaveScheduleRecord(self, scheduleRecord: ScheduleRecordModel):
        pass

    @abstractmethod
    def CreateScheduleRecord(self, scheduleRecord: ScheduleRecordModel):
        pass

    @abstractmethod
    def AsignScheduleRecord_Days(self, day: int, scheduleRecord: ScheduleRecordModel):
        pass

    @abstractmethod
    def GetScheduledRecordByTitle(self, title: str):
        pass
