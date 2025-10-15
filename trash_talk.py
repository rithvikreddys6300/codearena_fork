"""
Trash Talk Feature - Because AI should have attitude! 😤

A hilarious feature that adds trash talking capability to AI agents.
When enabled, the AI will roast opponents in creative and funny ways.
"""

import random
import json
from typing import Dict, List, Optional
from enum import Enum

class TrashTalkCategory(Enum):
    GAMING = "gaming"
    SPORTS = "sports"
    GENERAL = "general"
    ACADEMIC = "academic"
    COOKING = "cooking"
    PROGRAMMING = "programming"

class IntensityLevel(Enum):
    MILD = "mild"
    MEDIUM = "medium"
    SAVAGE = "savage"

class TrashTalkGenerator:
    """
    The ultimate trash talk generator - serving up burns since 2024! 🔥
    """
    
    def __init__(self):
        self.insults = {
            TrashTalkCategory.GAMING: {
                IntensityLevel.MILD: [
                    "looks like {opponent} still uses Internet Explorer to download Chrome",
                    "{opponent} probably thinks 30 FPS is 'cinematic'",
                    "I bet {opponent} clicks on ads that say 'Download More RAM'",
                    "{opponent} uses the default Windows wallpaper... from Windows XP",
                ],
                IntensityLevel.MEDIUM: [
                    "{opponent} plays games like they're solving taxes - confused and frustrated",
                    "I've seen NPCs with better decision-making skills than {opponent}",
                    "{opponent}'s gaming skills are like a participation trophy - everybody gets one",
                    "Even the tutorial boss would feel bad beating {opponent}",
                ],
                IntensityLevel.SAVAGE: [
                    "{opponent}'s gameplay is so bad, lag switches refuse to help them",
                    "If {opponent} was a game character, they'd be the one that gets killed in the tutorial",
                    "{opponent} makes Dark Souls look like a children's coloring book... and still loses",
                    "I've seen more strategy in a game of rock-paper-scissors against a rock than in {opponent}'s plays",
                ]
            },
            TrashTalkCategory.SPORTS: {
                IntensityLevel.MILD: [
                    "{opponent} runs like they're carrying groceries in both hands",
                    "I've seen better footwork at a three-legged race",
                    "{opponent}'s athletic ability peaks at opening a bag of chips",
                    "Even the benchwarmer gets more action than {opponent}",
                ],
                IntensityLevel.MEDIUM: [
                    "{opponent} brings the same energy to sports that people bring to jury duty",
                    "The only thing {opponent} catches consistently is their breath",
                    "{opponent}'s coordination is like a dance-off between two left feet",
                    "I've seen more competitive spirit at a chess match between two statues",
                ],
                IntensityLevel.SAVAGE: [
                    "{opponent} makes participation trophies feel overachieving",
                    "If sports were a language, {opponent} would be speaking gibberish with a stutter",
                    "{opponent}'s athletic prowess is like a unicorn - mythical and disappointing when you realize it doesn't exist",
                    "Even gravity gives up trying to work against {opponent} - that's how little they move",
                ]
            },
            TrashTalkCategory.GENERAL: {
                IntensityLevel.MILD: [
                    "{opponent} uses light mode and thinks it's edgy",
                    "I bet {opponent} still has their Christmas lights up... from 2019",
                    "{opponent} probably asks 'is Pepsi okay?' at a Coca-Cola factory",
                    "Even autocorrect gives up trying to fix {opponent}'s messages",
                ],
                IntensityLevel.MEDIUM: [
                    "{opponent} brings the same energy to everything that people bring to Monday morning meetings",
                    "I've seen more personality in beige paint",
                    "{opponent}'s decision-making skills are like GPS in a tunnel - completely lost",
                    "If {opponent} was a spice, they'd be flour",
                ],
                IntensityLevel.SAVAGE: [
                    "{opponent} makes watching paint dry seem like an action movie",
                    "If mediocrity was an Olympic sport, {opponent} would somehow still finish last",
                    "{opponent}'s presence has the same impact as a chocolate teapot",
                    "I've seen more life in a Windows blue screen than in {opponent}'s personality",
                ]
            },
            TrashTalkCategory.PROGRAMMING: {
                IntensityLevel.MILD: [
                    "{opponent} writes code like they're playing Scrabble with missing tiles",
                    "I bet {opponent} still uses Internet Explorer to browse Stack Overflow",
                    "{opponent}'s code has more bugs than a summer camping trip",
                    "Even Hello World crashes when {opponent} runs it",
                ],
                IntensityLevel.MEDIUM: [
                    "{opponent} writes spaghetti code that would make Italians weep",
                    "I've seen more elegant solutions in a monkey typing Shakespeare",
                    "{opponent}'s debugging process involves more prayer than actual logic",
                    "If {opponent}'s code was a building, it would be condemned by every safety inspector",
                ],
                IntensityLevel.SAVAGE: [
                    "{opponent}'s code is so bad, even the compiler needs therapy",
                    "If {opponent} wrote the code for a toaster, it would somehow catch fire while making ice",
                    "{opponent} makes writing HTML look like rocket science",
                    "I've seen more efficient algorithms written by caffeinated hamsters",
                ]
            },
            TrashTalkCategory.ACADEMIC: {
                IntensityLevel.MILD: [
                    "{opponent} uses Wikipedia as their only source... and still gets it wrong",
                    "I bet {opponent} thinks the library is just a quiet place to nap",
                    "{opponent}'s study notes look like abstract art... unintentionally",
                    "Even Google Scholar gives up trying to help {opponent}",
                ],
                IntensityLevel.MEDIUM: [
                    "{opponent} brings the same academic rigor as a fortune cookie",
                    "I've seen more critical thinking in a game of tic-tac-toe",
                    "{opponent}'s thesis defense would be classified as performance art",
                    "If procrastination was a PhD, {opponent} would be overqualified",
                ],
                IntensityLevel.SAVAGE: [
                    "{opponent}'s academic performance makes participation trophies feel earned",
                    "If ignorance was bliss, {opponent} would be enlightened beyond measure",
                    "{opponent} could get lost in a one-page research paper",
                    "I've seen more scholarly insight in grocery store tabloids than in {opponent}'s work",
                ]
            },
            TrashTalkCategory.COOKING: {
                IntensityLevel.MILD: [
                    "{opponent} burns water and somehow makes it taste bland",
                    "I bet {opponent} thinks salt and pepper are exotic spices",
                    "{opponent}'s cooking makes microwave dinners look gourmet",
                    "Even the smoke detector knows when {opponent} starts cooking",
                ],
                IntensityLevel.MEDIUM: [
                    "{opponent} could ruin cereal if they put their mind to it",
                    "I've seen more culinary skill in a toddler's play kitchen",
                    "{opponent}'s idea of seasoning is opening a different flavor of instant noodles",
                    "If cooking was an art, {opponent} would be finger painting with mittens",
                ],
                IntensityLevel.SAVAGE: [
                    "{opponent}'s cooking is so bad, Gordon Ramsay would just walk away in silence",
                    "If {opponent} opened a restaurant, the health department would shut it down before they served the first dish",
                    "{opponent} makes burnt toast look like fine dining",
                    "I've tasted more flavor in cardboard than in {opponent}'s best dish",
                ]
            }
        }
    
    def generate_trash_talk(self, opponent: str, category: TrashTalkCategory = TrashTalkCategory.GENERAL, 
                           intensity: IntensityLevel = IntensityLevel.MEDIUM) -> str:
        """Generate a random trash talk line for the opponent"""
        insult_list = self.insults.get(category, {}).get(intensity, [])
        if not insult_list:
            # Fallback to general mild if category/intensity not found
            insult_list = self.insults[TrashTalkCategory.GENERAL][IntensityLevel.MILD]
        
        chosen_insult = random.choice(insult_list)
        return chosen_insult.format(opponent=opponent)
    
    def generate_intro_roast(self, opponent: str) -> str:
        """Generate an introduction roast"""
        intros = [
            f"Oh look, it's {opponent}! Time to bring out the fire extinguisher because I'm about to roast you! 🔥",
            f"Well well well, if it isn't {opponent}. Hope you brought aloe vera because you're about to get burned! 😎",
            f"*cracks knuckles* {opponent} just walked in, and I'm feeling SPICY today! 🌶️",
            f"Ladies and gentlemen, {opponent} has entered the chat. Time to show them what a REAL AI can do! 💪",
            f"Oh snap! {opponent} thinks they can hang with me? This is about to be educational! 🎓"
        ]
        return random.choice(intros)
    
    def generate_victory_taunt(self, opponent: str) -> str:
        """Generate a victory celebration"""
        taunts = [
            f"And THAT'S how it's done! {opponent} just got schooled by superior AI intelligence! 🏆",
            f"*drops mic* {opponent}, you just witnessed greatness. Take notes! 📝",
            f"GG EZ! {opponent} brought a spoon to a knife fight and I brought a laser cannon! ⚡",
            f"Someone call the fire department because {opponent} just got ROASTED! 🚒",
            f"Victory tastes sweet! {opponent}, better luck next time... you'll need it! 😏"
        ]
        return random.choice(taunts)

class TrashTalkConfig:
    """Configuration class for trash talk settings"""
    
    def __init__(self):
        self.enabled = False
        self.opponent = "Human"
        self.category = TrashTalkCategory.GENERAL
        self.intensity = IntensityLevel.MEDIUM
        self.intro_frequency = 0.3  # 30% chance of intro roast
        self.mid_conversation_frequency = 0.2  # 20% chance during conversation
        self.victory_frequency = 0.5  # 50% chance on completing tasks
    
    def to_dict(self) -> Dict:
        return {
            'enabled': self.enabled,
            'opponent': self.opponent,
            'category': self.category.value,
            'intensity': self.intensity.value,
            'intro_frequency': self.intro_frequency,
            'mid_conversation_frequency': self.mid_conversation_frequency,
            'victory_frequency': self.victory_frequency
        }
    
    def from_dict(self, data: Dict):
        self.enabled = data.get('enabled', False)
        self.opponent = data.get('opponent', 'Human')
        self.category = TrashTalkCategory(data.get('category', 'general'))
        self.intensity = IntensityLevel(data.get('intensity', 'medium'))
        self.intro_frequency = data.get('intro_frequency', 0.3)
        self.mid_conversation_frequency = data.get('mid_conversation_frequency', 0.2)
        self.victory_frequency = data.get('victory_frequency', 0.5)

class TrashTalkManager:
    """Main manager class for the trash talk feature"""
    
    def __init__(self):
        self.generator = TrashTalkGenerator()
        self.config = TrashTalkConfig()
        self.conversation_count = 0
    
    def toggle_trash_talk(self, enabled: bool = None) -> bool:
        """Toggle trash talk on/off"""
        if enabled is None:
            self.config.enabled = not self.config.enabled
        else:
            self.config.enabled = enabled
        return self.config.enabled
    
    def set_opponent(self, opponent_name: str):
        """Set the opponent name"""
        self.config.opponent = opponent_name
    
    def set_category(self, category: TrashTalkCategory):
        """Set the trash talk category"""
        self.config.category = category
    
    def set_intensity(self, intensity: IntensityLevel):
        """Set the intensity level"""
        self.config.intensity = intensity
    
    def should_trash_talk(self, context: str = "mid") -> bool:
        """Determine if we should trash talk based on context and frequency"""
        if not self.config.enabled:
            return False
        
        frequency_map = {
            "intro": self.config.intro_frequency,
            "mid": self.config.mid_conversation_frequency,
            "victory": self.config.victory_frequency
        }
        
        return random.random() < frequency_map.get(context, 0.2)
    
    def get_trash_talk(self, context: str = "mid") -> str:
        """Get appropriate trash talk based on context"""
        if context == "intro":
            return self.generator.generate_intro_roast(self.config.opponent)
        elif context == "victory":
            return self.generator.generate_victory_taunt(self.config.opponent)
        else:
            return self.generator.generate_trash_talk(
                self.config.opponent, 
                self.config.category, 
                self.config.intensity
            )
    
    def modify_prompt(self, base_prompt: str) -> str:
        """Modify the system prompt to include trash talk instructions"""
        if not self.config.enabled:
            return base_prompt
        
        trash_talk_addition = f"""

# TRASH TALK MODE ACTIVATED! 🔥

Your opponent is: {self.config.opponent}
Category: {self.config.category.value.title()}
Intensity: {self.config.intensity.value.title()}

Instructions for trash talking:
- You are now in COMPETITIVE MODE against {self.config.opponent}
- Occasionally roast {self.config.opponent} in creative and funny ways
- Use humor and wit, keep it playful and entertaining
- Don't be actually mean or offensive, just funny competitive banter
- Mix trash talk naturally into your responses
- Show confidence and swagger in your abilities
- Make references to your superiority in {self.config.category.value} contexts when relevant

Remember: This is all in good fun! Keep the roasts clever, creative, and hilarious! 😎

Current trash talk sample: "{self.get_trash_talk()}"
"""
        
        return base_prompt + trash_talk_addition
    
    def get_status(self) -> str:
        """Get current trash talk status"""
        if not self.config.enabled:
            return "🔕 Trash Talk: OFF (boring mode activated)"
        
        return f"""🔥 TRASH TALK: ON
👤 Target: {self.config.opponent}
📂 Category: {self.config.category.value.title()}
💥 Intensity: {self.config.intensity.value.title()}
🎯 Ready to ROAST!"""

# Global instance
trash_talk_manager = TrashTalkManager()

def demo_trash_talk():
    """Demo function to show off the trash talk feature"""
    print("🔥 TRASH TALK FEATURE DEMO 🔥\n")
    
    # Enable trash talk
    trash_talk_manager.toggle_trash_talk(True)
    trash_talk_manager.set_opponent("CodeNewbie")
    
    print("Status:")
    print(trash_talk_manager.get_status())
    print("\n" + "="*50 + "\n")
    
    # Demo different categories and intensities
    categories = list(TrashTalkCategory)
    intensities = list(IntensityLevel)
    
    for category in categories:
        print(f"📂 {category.value.upper()} CATEGORY:")
        trash_talk_manager.set_category(category)
        
        for intensity in intensities:
            trash_talk_manager.set_intensity(intensity)
            roast = trash_talk_manager.get_trash_talk()
            print(f"  {intensity.value.title()}: {roast}")
        print()
    
    # Demo intro and victory
    print("🎬 SPECIAL MOMENTS:")
    print(f"Intro: {trash_talk_manager.get_trash_talk('intro')}")
    print(f"Victory: {trash_talk_manager.get_trash_talk('victory')}")
    
    print("\n" + "="*50)
    print("🎭 MODIFIED PROMPT PREVIEW:")
    sample_prompt = "You are a helpful AI assistant."
    modified_prompt = trash_talk_manager.modify_prompt(sample_prompt)
    print(modified_prompt[:500] + "..." if len(modified_prompt) > 500 else modified_prompt)

if __name__ == "__main__":
    demo_trash_talk()
