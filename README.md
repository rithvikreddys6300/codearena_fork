# Trash Talk Feature 🔥

A hilarious AI feature that adds competitive trash-talking capabilities to AI agents. When enabled, the AI will roast opponents in creative and funny ways across different categories and intensity levels.

## Features

- **Toggle On/Off**: Easy enable/disable functionality
- **Opponent Configuration**: Set custom opponent names
- **Multiple Categories**: Gaming, Sports, Programming, Academic, Cooking, General
- **Intensity Levels**: Mild (friendly), Medium (spicy), Savage (no mercy)
- **Context-Aware**: Different roasts for intros, mid-conversation, and victories
- **Randomized Content**: Hundreds of unique insults to keep it fresh
- **Prompt Integration**: Seamlessly modifies AI prompts to include trash talk personality

## Quick Start

### Basic Usage

```python
from trash_talk import trash_talk_manager, TrashTalkCategory, IntensityLevel

# Enable trash talk
trash_talk_manager.toggle_trash_talk(True)

# Set your opponent
trash_talk_manager.set_opponent("CodeNewbie")

# Configure category and intensity
trash_talk_manager.set_category(TrashTalkCategory.PROGRAMMING)
trash_talk_manager.set_intensity(IntensityLevel.SAVAGE)

# Generate a roast
roast = trash_talk_manager.get_trash_talk()
print(roast)
# Output: "CodeNewbie's code is so bad, even the compiler needs therapy"

# Check status
print(trash_talk_manager.get_status())
```

### Command Line Interface

```bash
# Enable with specific settings
python trash_talk_cli.py --enable --opponent "BuggyProgrammer" --category programming --intensity savage

# Generate roasts
python trash_talk_cli.py --roast
python trash_talk_cli.py --intro
python trash_talk_cli.py --victory

# Check status
python trash_talk_cli.py --status

# Run demo
python trash_talk_cli.py --demo
```

### Interactive Demo

```bash
python interactive_trash_talk.py
```

## Categories & Examples

### 🎮 Gaming
- **Mild**: "looks like {opponent} still uses Internet Explorer to download Chrome"
- **Savage**: "{opponent}'s gameplay is so bad, lag switches refuse to help them"

### 💻 Programming
- **Mild**: "{opponent} writes code like they're playing Scrabble with missing tiles"
- **Savage**: "If {opponent} wrote the code for a toaster, it would somehow catch fire while making ice"

### 🏃 Sports
- **Mild**: "{opponent} runs like they're carrying groceries in both hands"
- **Savage**: "Even gravity gives up trying to work against {opponent}"

### 🎓 Academic
- **Mild**: "{opponent} uses Wikipedia as their only source... and still gets it wrong"
- **Savage**: "I've seen more scholarly insight in grocery store tabloids than in {opponent}'s work"

### 👨‍🍳 Cooking
- **Mild**: "{opponent} burns water and somehow makes it taste bland"
- **Savage**: "{opponent}'s cooking is so bad, Gordon Ramsay would just walk away in silence"

### 💬 General
- **Mild**: "{opponent} uses light mode and thinks it's edgy"
- **Savage**: "{opponent} makes watching paint dry seem like an action movie"

## API Reference

### TrashTalkManager

Main class for managing trash talk functionality.

```python
# Toggle trash talk
enabled = trash_talk_manager.toggle_trash_talk(True)

# Configure settings
trash_talk_manager.set_opponent("OpponentName")
trash_talk_manager.set_category(TrashTalkCategory.GAMING)
trash_talk_manager.set_intensity(IntensityLevel.MEDIUM)

# Generate trash talk
roast = trash_talk_manager.get_trash_talk("mid")  # context: "intro", "mid", "victory"

# Modify AI prompts
modified_prompt = trash_talk_manager.modify_prompt(base_prompt)

# Get status
status = trash_talk_manager.get_status()
```

### Categories

```python
from trash_talk import TrashTalkCategory

TrashTalkCategory.GAMING
TrashTalkCategory.SPORTS
TrashTalkCategory.PROGRAMMING
TrashTalkCategory.ACADEMIC
TrashTalkCategory.COOKING
TrashTalkCategory.GENERAL
```

### Intensity Levels

```python
from trash_talk import IntensityLevel

IntensityLevel.MILD      # Friendly banter
IntensityLevel.MEDIUM    # Solid burns
IntensityLevel.SAVAGE    # Nuclear roasts
```

## Integration with AI Systems

The trash talk feature can be integrated into any AI system by modifying the system prompt:

```python
# Original prompt
base_prompt = "You are a helpful AI assistant."

# Enable trash talk
trash_talk_manager.toggle_trash_talk(True)
trash_talk_manager.set_opponent("User")

# Get modified prompt
enhanced_prompt = trash_talk_manager.modify_prompt(base_prompt)

# The AI will now occasionally roast the opponent while being helpful
```

## Configuration Management

### Export/Import Settings

```bash
# Export current config
python trash_talk_cli.py --export my_config.json

# Import config
python trash_talk_cli.py --import my_config.json
```

### Frequency Settings

Control how often trash talk appears:

```python
config = trash_talk_manager.config

config.intro_frequency = 0.3          # 30% chance on conversation start
config.mid_conversation_frequency = 0.2  # 20% chance during conversation
config.victory_frequency = 0.5         # 50% chance on task completion
```

## Safety & Guidelines

- **Keep it Fun**: All trash talk is designed to be humorous, not genuinely offensive
- **Context Appropriate**: Use appropriate intensity levels for your audience
- **Toggle Off**: Easy disable when professional tone is needed
- **Customizable**: Adjust frequency and intensity to match your needs

## Examples in Action

### Gaming Session
```python
trash_talk_manager.toggle_trash_talk(True)
trash_talk_manager.set_opponent("PlayerTwo")
trash_talk_manager.set_category(TrashTalkCategory.GAMING)
trash_talk_manager.set_intensity(IntensityLevel.MEDIUM)

print(trash_talk_manager.get_trash_talk("intro"))
# "Well well well, if it isn't PlayerTwo. Hope you brought aloe vera because you're about to get burned! 😎"

print(trash_talk_manager.get_trash_talk())
# "PlayerTwo plays games like they're solving taxes - confused and frustrated"

print(trash_talk_manager.get_trash_talk("victory"))
# "GG EZ! PlayerTwo brought a spoon to a knife fight and I brought a laser cannon! ⚡"
```

### Code Review Mode
```python
trash_talk_manager.set_category(TrashTalkCategory.PROGRAMMING)
trash_talk_manager.set_intensity(IntensityLevel.SAVAGE)

# AI reviewing code with attitude
roast = trash_talk_manager.get_trash_talk()
# "Developer's code has more bugs than a summer camping trip"
```

## Files

- `trash_talk.py` - Main feature implementation
- `trash_talk_cli.py` - Command line interface
- `interactive_trash_talk.py` - Interactive demo
- `README.md` - This documentation

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

---

**Remember**: This is all about having fun! Keep the roasting playful and enjoy the competitive banter! 🔥😎
