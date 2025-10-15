"""
Example: Trash Talk Integration with Chatbot

This example shows how to integrate the trash talk feature
with a simple chatbot system.
"""

from trash_talk import trash_talk_manager, TrashTalkCategory, IntensityLevel

class TrashTalkingChatbot:
    def __init__(self, name="AI Assistant"):
        self.name = name
        self.base_personality = "I am a helpful AI assistant."
        
    def enable_trash_talk(self, opponent="Human", category=TrashTalkCategory.GENERAL, 
                         intensity=IntensityLevel.MEDIUM):
        """Enable trash talk mode for this chatbot"""
        trash_talk_manager.toggle_trash_talk(True)
        trash_talk_manager.set_opponent(opponent)
        trash_talk_manager.set_category(category)
        trash_talk_manager.set_intensity(intensity)
        
        print(f"🔥 {self.name} entered TRASH TALK MODE!")
        print(f"Target: {opponent}")
        print(f"Category: {category.value.title()}")
        print(f"Intensity: {intensity.value.title()}")
        print()
    
    def disable_trash_talk(self):
        """Disable trash talk mode"""
        trash_talk_manager.toggle_trash_talk(False)
        print(f"🔕 {self.name} returned to professional mode.")
    
    def get_response(self, user_input, context="mid"):
        """Generate a response with optional trash talk"""
        
        # Base response logic (simplified)
        if "hello" in user_input.lower():
            base_response = "Hello! How can I help you today?"
            if trash_talk_manager.config.enabled and context == "intro":
                trash_talk = trash_talk_manager.get_trash_talk("intro")
                return f"{trash_talk}\n\nBut seriously, {base_response.lower()}"
        
        elif "help" in user_input.lower():
            base_response = "I'm here to assist you with various tasks."
            if trash_talk_manager.config.enabled and trash_talk_manager.should_trash_talk("mid"):
                trash_talk = trash_talk_manager.get_trash_talk()
                return f"{base_response} {trash_talk} But don't worry, I'll still help you out! 😎"
        
        elif "bye" in user_input.lower() or "goodbye" in user_input.lower():
            base_response = "Goodbye! Have a great day!"
            if trash_talk_manager.config.enabled and trash_talk_manager.should_trash_talk("victory"):
                trash_talk = trash_talk_manager.get_trash_talk("victory")
                return f"{base_response}\n\n{trash_talk}"
        
        else:
            base_response = "I understand you're asking about something. Let me help you with that."
            if trash_talk_manager.config.enabled and trash_talk_manager.should_trash_talk("mid"):
                trash_talk = trash_talk_manager.get_trash_talk()
                return f"{base_response} {trash_talk}"
        
        return base_response

def demo_chatbot():
    print("🤖 TRASH TALKING CHATBOT DEMO 🤖\n")
    
    # Create chatbot
    bot = TrashTalkingChatbot("RoastBot")
    
    # Demo 1: Normal mode
    print("="*50)
    print("DEMO 1: Normal Professional Mode")
    print("="*50)
    print(f"User: hello")
    print(f"Bot: {bot.get_response('hello', 'intro')}")
    print()
    
    print(f"User: can you help me?")
    print(f"Bot: {bot.get_response('can you help me?')}")
    print()
    
    # Demo 2: Gaming trash talk mode
    print("="*50)
    print("DEMO 2: Gaming Trash Talk Mode")
    print("="*50)
    bot.enable_trash_talk("ProGamer2024", TrashTalkCategory.GAMING, IntensityLevel.MEDIUM)
    
    print(f"User: hello")
    print(f"Bot: {bot.get_response('hello', 'intro')}")
    print()
    
    print(f"User: I need help with my game")
    response = bot.get_response('I need help with my game')
    print(f"Bot: {response}")
    print()
    
    print(f"User: goodbye")
    print(f"Bot: {bot.get_response('goodbye')}")
    print()
    
    # Demo 3: Programming savage mode
    print("="*50)
    print("DEMO 3: Programming SAVAGE Mode")
    print("="*50)
    bot.enable_trash_talk("CodeNewbie", TrashTalkCategory.PROGRAMMING, IntensityLevel.SAVAGE)
    
    print(f"User: hello")
    print(f"Bot: {bot.get_response('hello', 'intro')}")
    print()
    
    print(f"User: help me debug my code")
    response = bot.get_response('help me debug my code')
    print(f"Bot: {response}")
    print()
    
    print(f"User: bye")
    print(f"Bot: {bot.get_response('bye')}")
    print()
    
    # Back to normal
    bot.disable_trash_talk()

if __name__ == "__main__":
    demo_chatbot()
