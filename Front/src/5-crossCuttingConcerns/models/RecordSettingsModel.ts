import { VideoFormatsEnum } from "../enums/VideoFormatsEnum"


export class RecordSettingsModel {
    duration: number
    video_format: VideoFormatsEnum
    screen_height: number
    screen_weight: number
    fps: number
    directory: string
    id: number

    constructor(
        duration:number = 10, 
        video_format: VideoFormatsEnum = VideoFormatsEnum.XVID, 
        screen_height:number = 1080, 
        screen_weight:number = 1920, 
        fps:number = 20, 
        directory:string = "", 
        id:number = -1
    ) {
        this.directory = directory
        this.duration = duration
        this.fps = fps
        this.id = id
        this.screen_height = screen_height
        this.screen_weight = screen_weight
        this.video_format = video_format
    }
}