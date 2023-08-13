import sqlite3

from DataAccess.IRepository import IRepository
from Models.RecordSettings import RecordSettings
from Models.ScheduleRecord import ScheduleRecordModel

dateFormat = "%Y-%m-%d %H:%M:%S"
class SqlLiteDA(IRepository):
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        # Tabla para la configuración
        cursor.execute('''CREATE TABLE IF NOT EXISTS Configuracion
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           duration INTEGER,
                           video_format TEXT,
                           screen_height INTEGER,
                           screen_weight INTEGER,
                           fps INTEGER,
                           directory TEXT)''')

        # Tabla para grabaciones programadas
        cursor.execute('''CREATE TABLE IF NOT EXISTS ScheduleRecord
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           timeFrom TEXT,
                           timeTo TEXT,
                           title TEXT UNIQUE,
                           base_name TEXT UNIQUE,
                           onlyOnce BIT,
                           lastExecutionDate TEXT
                           )''')

        # Tabla de los días de la semana
        cursor.execute('''CREATE TABLE IF NOT EXISTS Days
                          (
                            id INTEGER PRIMARY KEY UNIQUE,
                            name TEXT UNIQUE
                           )''')

        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        for index, day in enumerate(days_of_week):
            cursor.execute("INSERT OR IGNORE INTO Days (id, name) VALUES (?, ?)", (index, day))

        # Tabla para asociar dias con grabaciones programadas
        cursor.execute('''CREATE TABLE IF NOT EXISTS ScheduleRecord_Days
                                  (
                                    id_scheduleRecord INTEGER,
                                    id_day INTEGER,
                                    FOREIGN KEY (id_scheduleRecord) REFERENCES ScheduleRecord(id),
                                    FOREIGN KEY (id_day) REFERENCES Days(id)
                                   )''')


        self.conn.commit()

    def SaveConfiguration(self, settings: RecordSettings):
        cursor = self.conn.cursor()
        cursor.execute('''UPDATE Configuracion 
                          SET duration = ?, video_format = ?, screen_height = ?, 
                              screen_weight = ?, fps = ?, directory = ? 
                          WHERE id = ?''',
                       (settings.duration, settings.video_format, settings.screen_height,
                        settings.screen_weight, settings.fps, settings.directory, settings.id))
        self.conn.commit()

    def CreateConfiguration(self, settings: RecordSettings):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO Configuracion (duration, video_format, screen_height, screen_weight, fps, directory)
                          VALUES (?, ?, ?, ?, ?, ?)''',
                       (settings.duration, settings.video_format, settings.screen_height,
                        settings.screen_weight, settings.fps, settings.directory))
        self.conn.commit()

    def GetSettings(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Configuracion")
        return cursor.fetchone()

    def ScheduleRecord(self, scheduledRecord: ScheduleRecordModel):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO ScheduleRecord (timeFrom, timeTo, title)
                          VALUES (?, ?, ?)''',
                       (scheduledRecord.timeFrom, scheduledRecord.timeTo, scheduledRecord.title))
        self.conn.commit()

    def CancelScheduledRecord(self, scheduledRecord: ScheduleRecordModel):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM ScheduleRecord WHERE id = ?", (scheduledRecord.id,))
        self.conn.commit()

    def GetMyScheduledRecords(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM ScheduleRecord")
        return cursor.fetchall()

    def SaveScheduleRecord(self, scheduleRecord: ScheduleRecordModel):
        cursor = self.conn.cursor()
        cursor.execute('''UPDATE ScheduleRecord 
                                  SET timeFrom = ?, timeTo = ?, title = ?, 
                                      base_name = ?, onlyOnce = ?, lastExecutionDate = ?
                                  WHERE id = ?''',
                       (
                           scheduleRecord.timeFrom,
                           scheduleRecord.timeTo,
                           scheduleRecord.title,
                           scheduleRecord.file_base_name,
                           scheduleRecord.onlyOnce,
                           scheduleRecord.lastExecutionDate,
                           scheduleRecord.id
                       ))
        self.conn.commit()
        pass

    def CreateScheduleRecord(self, scheduleRecord: ScheduleRecordModel):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO ScheduleRecord (timeFrom, timeTo, title, base_name, onlyOnce, lastExecutionDate)
                          VALUES (?, ?, ?, ?, ?, ?)''',
                       (
                        scheduleRecord.timeFrom.strftime(dateFormat),
                        scheduleRecord.timeTo.strftime(dateFormat),
                        scheduleRecord.title,
                        scheduleRecord.file_base_name,
                        1 if scheduleRecord.onlyOnce else 0,
                        scheduleRecord.lastExecutionDate
                        ))
        self.conn.commit()
        pass

    def GetScheduledRecordByTitle(self, title: str):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM ScheduleRecord WHERE title = ? LIMIT 1", (title,))
        return cursor.fetchall()[0]

    def AsignScheduleRecord_Days(self, Day: int, scheduleRecord: ScheduleRecordModel):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO ScheduleRecord_Days (id_day, id_scheduleRecord)
                                  VALUES (?, ?)''',
                       (
                           Day,
                           scheduleRecord.id
                       ))
        self.conn.commit()
        pass


    def __del__(self):
        self.conn.close()