from dataclasses import dataclass, field, asdict
from dataclasses_json import dataclass_json, config
from datetime import datetime
from typing import List, Optional

format = "%Y-%m-%d %H:%M:%S"
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

@dataclass_json
@dataclass
class ScheduleRecordModel:
    timeFrom: datetime
    timeTo: datetime
    video_title: Optional[str] = field(default_factory=lambda: datetime.now().strftime(format))
    file_base_name: Optional[str] = ""
    repetitionDays: List[str] = field(default_factory=list)
    onlyOnce: Optional[bool] = False

    id: int = field(default=-1, metadata=config(field_name="id"))
    lastExecutionDate: str = field(default="", metadata=config(field_name="lastExecutionDate"))

    def __post_init__(self):
        if not self.video_title:
            self.video_title = datetime.now().strftime(format)
