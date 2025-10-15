export enum TrashTalkCategory {
  GAMING = "gaming",
  SPORTS = "sports", 
  PROGRAMMING = "programming",
  ACADEMIC = "academic",
  COOKING = "cooking",
  GENERAL = "general"
}

export enum IntensityLevel {
  MILD = "mild",
  MEDIUM = "medium",
  SAVAGE = "savage"
}

export type TrashTalkContext = "intro" | "mid" | "victory";

export interface TrashTalkConfig {
  enabled: boolean;
  opponent: string;
  category: TrashTalkCategory;
  intensity: IntensityLevel;
  introFrequency: number;
  midConversationFrequency: number;
  victoryFrequency: number;
}

export interface TrashTalkResponse {
  message: string;
  context: TrashTalkContext;
  category: TrashTalkCategory;
  intensity: IntensityLevel;
}

export interface TrashTalkStatus extends TrashTalkConfig {
  lastRoast?: string;
  roastCount: number;
}
