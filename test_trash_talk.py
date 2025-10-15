"""
Test Suite for Trash Talk Feature

Run with: python3 test_trash_talk.py
"""

import unittest
from trash_talk import (
    TrashTalkGenerator, TrashTalkConfig, TrashTalkManager,
    TrashTalkCategory, IntensityLevel, trash_talk_manager
)

class TestTrashTalkGenerator(unittest.TestCase):
    
    def setUp(self):
        self.generator = TrashTalkGenerator()
    
    def test_generate_trash_talk(self):
        """Test basic trash talk generation"""
        roast = self.generator.generate_trash_talk("TestOpponent")
        self.assertIsInstance(roast, str)
        self.assertIn("TestOpponent", roast)
        self.assertGreater(len(roast), 10)
    
    def test_different_categories(self):
        """Test different categories generate different content"""
        gaming_roast = self.generator.generate_trash_talk(
            "Player", TrashTalkCategory.GAMING, IntensityLevel.MILD
        )
        programming_roast = self.generator.generate_trash_talk(
            "Player", TrashTalkCategory.PROGRAMMING, IntensityLevel.MILD
        )
        # Both should contain the opponent name
        self.assertIn("Player", gaming_roast)
        self.assertIn("Player", programming_roast)
    
    def test_intro_roast(self):
        """Test intro roast generation"""
        intro = self.generator.generate_intro_roast("NewPlayer")
        self.assertIsInstance(intro, str)
        self.assertIn("NewPlayer", intro)
        self.assertTrue(any(emoji in intro for emoji in ["🔥", "😎", "🌶️", "💪", "🎓"]))
    
    def test_victory_taunt(self):
        """Test victory taunt generation"""
        victory = self.generator.generate_victory_taunt("Loser")
        self.assertIsInstance(victory, str)
        self.assertIn("Loser", victory)
        self.assertTrue(any(emoji in victory for emoji in ["🏆", "📝", "⚡", "🚒", "😏"]))

class TestTrashTalkConfig(unittest.TestCase):
    
    def setUp(self):
        self.config = TrashTalkConfig()
    
    def test_default_settings(self):
        """Test default configuration"""
        self.assertFalse(self.config.enabled)
        self.assertEqual(self.config.opponent, "Human")
        self.assertEqual(self.config.category, TrashTalkCategory.GENERAL)
        self.assertEqual(self.config.intensity, IntensityLevel.MEDIUM)
    
    def test_to_dict_from_dict(self):
        """Test serialization and deserialization"""
        # Modify config
        self.config.enabled = True
        self.config.opponent = "TestUser"
        self.config.category = TrashTalkCategory.GAMING
        self.config.intensity = IntensityLevel.SAVAGE
        
        # Serialize
        data = self.config.to_dict()
        self.assertIsInstance(data, dict)
        self.assertTrue(data['enabled'])
        self.assertEqual(data['opponent'], "TestUser")
        
        # Create new config and deserialize
        new_config = TrashTalkConfig()
        new_config.from_dict(data)
        
        self.assertEqual(new_config.enabled, self.config.enabled)
        self.assertEqual(new_config.opponent, self.config.opponent)
        self.assertEqual(new_config.category, self.config.category)
        self.assertEqual(new_config.intensity, self.config.intensity)

class TestTrashTalkManager(unittest.TestCase):
    
    def setUp(self):
        self.manager = TrashTalkManager()
        # Reset to known state
        self.manager.toggle_trash_talk(False)
        self.manager.set_opponent("TestOpponent")
    
    def test_toggle_functionality(self):
        """Test toggle on/off functionality"""
        # Should be off initially
        self.assertFalse(self.manager.config.enabled)
        
        # Toggle on
        result = self.manager.toggle_trash_talk(True)
        self.assertTrue(result)
        self.assertTrue(self.manager.config.enabled)
        
        # Toggle off
        result = self.manager.toggle_trash_talk(False)
        self.assertFalse(result)
        self.assertFalse(self.manager.config.enabled)
        
        # Toggle without parameter
        result = self.manager.toggle_trash_talk()
        self.assertTrue(result)  # Should toggle to True
    
    def test_configuration_methods(self):
        """Test configuration setter methods"""
        self.manager.set_opponent("NewOpponent")
        self.assertEqual(self.manager.config.opponent, "NewOpponent")
        
        self.manager.set_category(TrashTalkCategory.PROGRAMMING)
        self.assertEqual(self.manager.config.category, TrashTalkCategory.PROGRAMMING)
        
        self.manager.set_intensity(IntensityLevel.SAVAGE)
        self.assertEqual(self.manager.config.intensity, IntensityLevel.SAVAGE)
    
    def test_should_trash_talk(self):
        """Test trash talk frequency logic"""
        # Should never trash talk when disabled
        self.manager.toggle_trash_talk(False)
        self.assertFalse(self.manager.should_trash_talk("intro"))
        self.assertFalse(self.manager.should_trash_talk("mid"))
        self.assertFalse(self.manager.should_trash_talk("victory"))
        
        # When enabled, should be probabilistic
        self.manager.toggle_trash_talk(True)
        # Set frequencies to 100% for testing
        self.manager.config.intro_frequency = 1.0
        self.manager.config.mid_conversation_frequency = 1.0
        self.manager.config.victory_frequency = 1.0
        
        self.assertTrue(self.manager.should_trash_talk("intro"))
        self.assertTrue(self.manager.should_trash_talk("mid"))
        self.assertTrue(self.manager.should_trash_talk("victory"))
    
    def test_get_trash_talk_contexts(self):
        """Test different context trash talk generation"""
        self.manager.toggle_trash_talk(True)
        
        intro = self.manager.get_trash_talk("intro")
        mid = self.manager.get_trash_talk("mid")
        victory = self.manager.get_trash_talk("victory")
        
        self.assertIsInstance(intro, str)
        self.assertIsInstance(mid, str)
        self.assertIsInstance(victory, str)
        
        self.assertIn("TestOpponent", intro)
        self.assertIn("TestOpponent", mid)
        self.assertIn("TestOpponent", victory)
    
    def test_modify_prompt(self):
        """Test prompt modification functionality"""
        base_prompt = "You are a helpful assistant."
        
        # When disabled, should return unchanged prompt
        self.manager.toggle_trash_talk(False)
        modified = self.manager.modify_prompt(base_prompt)
        self.assertEqual(modified, base_prompt)
        
        # When enabled, should add trash talk instructions
        self.manager.toggle_trash_talk(True)
        modified = self.manager.modify_prompt(base_prompt)
        self.assertIn(base_prompt, modified)
        self.assertIn("TRASH TALK MODE ACTIVATED", modified)
        self.assertIn("TestOpponent", modified)
    
    def test_get_status(self):
        """Test status reporting"""
        # Disabled status
        self.manager.toggle_trash_talk(False)
        status = self.manager.get_status()
        self.assertIn("OFF", status)
        
        # Enabled status
        self.manager.toggle_trash_talk(True)
        status = self.manager.get_status()
        self.assertIn("ON", status)
        self.assertIn("TestOpponent", status)

class TestIntegration(unittest.TestCase):
    """Integration tests"""
    
    def test_global_manager_instance(self):
        """Test the global manager instance works correctly"""
        # Reset state
        trash_talk_manager.toggle_trash_talk(False)
        
        # Test basic functionality
        self.assertFalse(trash_talk_manager.config.enabled)
        
        trash_talk_manager.toggle_trash_talk(True)
        trash_talk_manager.set_opponent("IntegrationTest")
        
        roast = trash_talk_manager.get_trash_talk()
        self.assertIn("IntegrationTest", roast)
        
        # Reset for other tests
        trash_talk_manager.toggle_trash_talk(False)

def run_all_tests():
    """Run all tests and display results"""
    print("🧪 TRASH TALK FEATURE TEST SUITE 🧪\n")
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_classes = [
        TestTrashTalkGenerator,
        TestTrashTalkConfig,
        TestTrashTalkManager,
        TestIntegration
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Summary
    print(f"\n{'='*60}")
    if result.wasSuccessful():
        print("🎉 ALL TESTS PASSED! Trash talk feature is ready to roast! 🔥")
    else:
        print(f"❌ {len(result.failures)} test(s) failed, {len(result.errors)} error(s)")
        
        if result.failures:
            print("\nFailures:")
            for test, trace in result.failures:
                print(f"  - {test}: {trace.split(chr(10))[-2]}")
        
        if result.errors:
            print("\nErrors:")
            for test, trace in result.errors:
                print(f"  - {test}: {trace.split(chr(10))[-2]}")
    
    print(f"{'='*60}")
    return result.wasSuccessful()

if __name__ == "__main__":
    run_all_tests()
