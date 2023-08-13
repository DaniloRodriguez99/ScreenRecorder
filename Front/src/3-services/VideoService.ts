import { VideoFormatsEnum } from "../5-crossCuttingConcerns/enums/VideoFormatsEnum";

export class VideoFormatsService {

    static getAllVideoFormats(): { key: string, value: number }[] {
        return Object.entries(VideoFormatsEnum)
            .filter(([key, value]) => !isNaN(Number(value))) // Filtrar sólo los valores numéricos del enum
            .map(([key, value]) => ({ key, value: Number(value) }));
    }
    
}