import { TrashTalkCategory, IntensityLevel, TrashTalkContext, TrashTalkConfig, TrashTalkStatus } from "@/types/trash-talk";

// Trash talk data - converted from Python implementation
const TRASH_TALK_DATA = {
  [TrashTalkCategory.GAMING]: {
    [IntensityLevel.MILD]: [
      "looks like {opponent} still uses Internet Explorer to download Chrome",
      "{opponent} plays games like they're reading the manual for the first time",
      "I've seen NPCs with better reflexes than {opponent}",
      "{opponent} needs training wheels for their gaming chair"
    ],
    [IntensityLevel.MEDIUM]: [
      "{opponent} plays games like they're solving taxes - confused and frustrated",
      "{opponent}'s gaming skills peaked at Solitaire and it's been downhill ever since",
      "Even the tutorial boss would go easy on {opponent}",
      "{opponent} makes watching paint dry look exciting"
    ],
    [IntensityLevel.SAVAGE]: [
      "{opponent}'s gameplay is so bad, lag switches refuse to help them",
      "{opponent} could lose at tic-tac-toe against a goldfish",
      "{opponent}'s gaming career has more crashes than Windows Vista",
      "{opponent} makes noobs look like esports legends"
    ]
  },
  [TrashTalkCategory.PROGRAMMING]: {
    [IntensityLevel.MILD]: [
      "{opponent} writes code like they're playing Scrabble with missing tiles",
      "{opponent}'s code has more bugs than a summer picnic",
      "{opponent} debugs code by praying to the computer gods",
      "{opponent} uses Stack Overflow more than their own brain"
    ],
    [IntensityLevel.MEDIUM]: [
      "{opponent}'s code is so messy, even spaghetti code looks organized",
      "{opponent} writes functions longer than a CVS receipt",
      "{opponent}'s variable names look like they typed with their feet",
      "{opponent}'s code has more patches than a quilt"
    ],
    [IntensityLevel.SAVAGE]: [
      "If {opponent} wrote the code for a toaster, it would somehow catch fire while making ice",
      "{opponent}'s code is so bad, even the compiler needs therapy",
      "{opponent} could crash a calculator by trying to divide by zero",
      "{opponent}'s programming skills make HTML look like rocket science"
    ]
  },
  [TrashTalkCategory.SPORTS]: {
    [IntensityLevel.MILD]: [
      "{opponent} runs like they're carrying groceries in both hands",
      "{opponent}'s athletic ability peaked in kindergarten",
      "{opponent} needs GPS to find the gym",
      "{opponent} considers walking to the fridge cardio"
    ],
    [IntensityLevel.MEDIUM]: [
      "{opponent} moves like they're stuck in quicksand",
      "{opponent}'s idea of a workout is opening a pickle jar",
      "{opponent} has the coordination of a newborn giraffe",
      "{opponent} makes participation trophies feel embarrassed"
    ],
    [IntensityLevel.SAVAGE]: [
      "Even gravity gives up trying to work against {opponent}",
      "{opponent} could lose a race against a sloth having an existential crisis",
      "{opponent}'s athletic performance makes couch potatoes look Olympic",
      "{opponent} needs a map and compass to navigate around a track"
    ]
  },
  [TrashTalkCategory.ACADEMIC]: {
    [IntensityLevel.MILD]: [
      "{opponent} uses Wikipedia as their only source... and still gets it wrong",
      "{opponent}'s study habits make procrastination look productive",
      "{opponent} needs Google to spell 'Google'",
      "{opponent}'s brain runs on dial-up internet"
    ],
    [IntensityLevel.MEDIUM]: [
      "{opponent}'s intellect has the depth of a puddle in the desert",
      "{opponent} makes multiple choice tests multiple guess tests",
      "{opponent}'s critical thinking skills are still under construction",
      "{opponent} needs subtitles for picture books"
    ],
    [IntensityLevel.SAVAGE]: [
      "I've seen more scholarly insight in grocery store tabloids than in {opponent}'s work",
      "{opponent} could fail an open book test even if the answers were highlighted",
      "{opponent}'s knowledge base is smaller than a tweet",
      "{opponent} makes rocks look intellectually stimulating"
    ]
  },
  [TrashTalkCategory.COOKING]: {
    [IntensityLevel.MILD]: [
      "{opponent} burns water and somehow makes it taste bland",
      "{opponent}'s cooking comes with a smoke alarm soundtrack",
      "{opponent} needs instructions to make ice cubes",
      "{opponent}'s kitchen skills peaked at microwave popcorn"
    ],
    [IntensityLevel.MEDIUM]: [
      "{opponent}'s cooking could be classified as biological warfare",
      "{opponent} makes Gordon Ramsay cry... and not tears of joy",
      "{opponent}'s recipes are sponsored by the fire department",
      "{opponent} considers takeout menus their cookbook collection"
    ],
    [IntensityLevel.SAVAGE]: [
      "{opponent}'s cooking is so bad, Gordon Ramsay would just walk away in silence",
      "{opponent} could ruin cereal and somehow make it too spicy",
      "{opponent}'s kitchen disasters have their own FEMA classification",
      "{opponent} makes military rations look gourmet"
    ]
  },
  [TrashTalkCategory.GENERAL]: {
    [IntensityLevel.MILD]: [
      "{opponent} uses light mode and thinks it's edgy",
      "{opponent} still asks 'Are you sure?' when deleting emails",
      "{opponent} types with two fingers and still makes typos",
      "{opponent}'s password is probably 'password123'"
    ],
    [IntensityLevel.MEDIUM]: [
      "{opponent} makes watching grass grow seem thrilling",
      "{opponent}'s personality has the excitement of unbuttered toast",
      "{opponent} could bore an insomniac to sleep",
      "{opponent}'s idea of living dangerously is using a pen instead of pencil"
    ],
    [IntensityLevel.SAVAGE]: [
      "{opponent} makes watching paint dry seem like an action movie",
      "{opponent}'s existence is so bland, vanilla feels insulted",
      "{opponent} could cure insomnia just by existing in the same room",
      "{opponent}'s life story would be titled 'Meh: A Journey to Nowhere'"
    ]
  }
};

const INTRO_ROASTS = [
  "Well well well, if it isn't {opponent}. Hope you brought aloe vera because you're about to get burned! 😎",
  "Oh look, {opponent} showed up! This should be easier than I thought... 🔥",
  "Hey {opponent}! Ready to get absolutely demolished? Don't worry, I'll go easy on you... NOT! 💀",
  "Uh oh, {opponent} is here. Someone call the ambulance, we're about to have a casualty! 🚨",
  "Breaking news: {opponent} about to get schooled! More details at never because it's too embarrassing! 📰"
];

const VICTORY_ROASTS = [
  "GG EZ! {opponent} brought a spoon to a knife fight and I brought a laser cannon! ⚡",
  "Another victory! {opponent}, you fought valiantly... just kidding, that was painful to watch! 🏆",
  "Flawless Victory! {opponent}, you can pick up your dignity at the lost and found... oh wait, they don't have it either! 👑",
  "BOOM! Headshot! {opponent} just got sent back to the tutorial! 💥",
  "Victory! {opponent}, that wasn't even a challenge. I've had tougher opponents in my sleep! 😴"
];

class TrashTalkManager {
  private config: TrashTalkConfig = {
    enabled: false,
    opponent: "Opponent",
    category: TrashTalkCategory.GENERAL,
    intensity: IntensityLevel.MEDIUM,
    introFrequency: 0.3,
    midConversationFrequency: 0.2,
    victoryFrequency: 0.5
  };

  private roastCount = 0;
  private lastRoast?: string;

  toggleTrashTalk(enabled: boolean): boolean {
    this.config.enabled = enabled;
    return this.config.enabled;
  }

  setOpponent(opponent: string): void {
    this.config.opponent = opponent;
  }

  setCategory(category: TrashTalkCategory): void {
    this.config.category = category;
  }

  setIntensity(intensity: IntensityLevel): void {
    this.config.intensity = intensity;
  }

  getTrashTalk(context: TrashTalkContext = "mid"): string {
    if (!this.config.enabled) {
      return "";
    }

    let roasts: string[];
    
    if (context === "intro") {
      roasts = INTRO_ROASTS;
    } else if (context === "victory") {
      roasts = VICTORY_ROASTS;
    } else {
      const categoryRoasts = TRASH_TALK_DATA[this.config.category];
      roasts = categoryRoasts[this.config.intensity];
    }

    const randomRoast = roasts[Math.floor(Math.random() * roasts.length)];
    const personalizedRoast = randomRoast.replace(/{opponent}/g, this.config.opponent);
    
    this.lastRoast = personalizedRoast;
    this.roastCount++;
    
    return personalizedRoast;
  }

  shouldGenerateTrashTalk(context: TrashTalkContext): boolean {
    if (!this.config.enabled) return false;

    const random = Math.random();
    switch (context) {
      case "intro":
        return random < this.config.introFrequency;
      case "mid":
        return random < this.config.midConversationFrequency;
      case "victory":
        return random < this.config.victoryFrequency;
      default:
        return false;
    }
  }

  modifyPrompt(basePrompt: string): string {
    if (!this.config.enabled) {
      return basePrompt;
    }

    const trashTalkPersonality = `
You are now in TRASH TALK MODE! 🔥 
Your opponent is ${this.config.opponent}. 
You should occasionally roast them in a funny, creative way while still being helpful.
Category focus: ${this.config.category}
Intensity level: ${this.config.intensity}
Keep it playful and humorous, not genuinely mean or offensive.
`;

    return basePrompt + "\n\n" + trashTalkPersonality;
  }

  getStatus(): TrashTalkStatus {
    return {
      ...this.config,
      lastRoast: this.lastRoast,
      roastCount: this.roastCount
    };
  }

  getConfig(): TrashTalkConfig {
    return { ...this.config };
  }

  updateConfig(newConfig: Partial<TrashTalkConfig>): void {
    this.config = { ...this.config, ...newConfig };
  }

  reset(): void {
    this.config = {
      enabled: false,
      opponent: "Opponent",
      category: TrashTalkCategory.GENERAL,
      intensity: IntensityLevel.MEDIUM,
      introFrequency: 0.3,
      midConversationFrequency: 0.2,
      victoryFrequency: 0.5
    };
    this.roastCount = 0;
    this.lastRoast = undefined;
  }

  exportConfig(): string {
    return JSON.stringify(this.getStatus(), null, 2);
  }

  importConfig(configJson: string): boolean {
    try {
      const importedConfig = JSON.parse(configJson);
      this.updateConfig(importedConfig);
      return true;
    } catch (error) {
      console.error("Failed to import config:", error);
      return false;
    }
  }
}

// Export singleton instance
export const trashTalkManager = new TrashTalkManager();
export default trashTalkManager;
