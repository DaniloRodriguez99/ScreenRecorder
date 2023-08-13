from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional

@dataclass_json
@dataclass
class RecordSettings:
    duration: Optional[int] = 6000
    video_format: Optional[str] = "XVID"
    screen_height: Optional[int] = 1080
    screen_weight: Optional[int] = 1920
    fps: Optional[int] = 20
    directory: Optional[str] = ""
    id: Optional[int] = -1
