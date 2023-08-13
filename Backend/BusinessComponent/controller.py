from datetime import datetime

from DataAccess.IRepository import IRepository
from Models.RecordSettings import RecordSettings
from Models.ScheduleRecord import ScheduleRecordModel


class MainController:

    def __init__(self, dataAccess: IRepository):
        self.dataAccess = dataAccess

    def SaveConfiguration(self, settings: RecordSettings):
        if int(settings.fps) < 0:
            pass
        if int(settings.duration) < 0:
            pass
        if settings.video_format == "":
            pass

        currentSettings: RecordSettings = self.GetSettings()
        if currentSettings is not None and currentSettings.id >= 0:
            self.dataAccess.SaveConfiguration(settings)
        else:
            self.dataAccess.CreateConfiguration(settings)


    def GetSettings(self) -> RecordSettings:
        settings = self.dataAccess.GetSettings()

        result = RecordSettings()

        if (settings is not None):
            result.id = settings[0]
            result.duration = settings[1]
            result.video_format = settings[2]
            result.screen_weight = settings[3]
            result.screen_height = settings[4]
            result.fps = settings[5]
            result.directory = settings[6]

        return result

    def ScheduleRecord(self, scheduledRecord: ScheduleRecordModel):
        if scheduledRecord.timeTo <= datetime.now():
            pass
        if scheduledRecord.timeFrom <= datetime.now():
            pass
        if scheduledRecord.timeFrom >= scheduledRecord.timeFrom:
            pass
        if scheduledRecord.title == "":
            pass

        self.dataAccess.ScheduleRecord(scheduledRecord)

    def CalcelScheduledRecord(self, scheduledRecord: ScheduleRecordModel):
        if scheduledRecord.id <= -1:
            pass

        self.dataAccess.CalcelScheduledRecord()

    def GetMyScheduledRecords(self):
        return self.dataAccess.GetMyScheduledRecords()

    def SaveScheduleRecord(self, scheduleRecord: ScheduleRecordModel):
        if scheduleRecord.title.replace(" ", "_") != "":
            pass
        if scheduleRecord.timeFrom > scheduleRecord.timeTo:
            pass

        if scheduleRecord is not None:
            if scheduleRecord.id >= 0:
                self.dataAccess.SaveScheduleRecord(scheduleRecord)
            else:
                self.dataAccess.CreateScheduleRecord(scheduleRecord)
                scheduleRecord.id = self.dataAccess.GetScheduledRecordByTitle(scheduleRecord.title)[0]

                for day in scheduleRecord.repetitionDays:
                    self.AsignScheduleRecord_Days(int(day), scheduleRecord)


    def AsignScheduleRecord_Days(self, Day: int, scheduleRecord: ScheduleRecordModel):
        self.dataAccess.AsignScheduleRecord_Days(Day, scheduleRecord)

