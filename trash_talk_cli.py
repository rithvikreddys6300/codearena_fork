#!/usr/bin/env python3
"""
Trash Talk CLI - Command Line Interface for the Trash Talk Feature

Usage examples:
  python trash_talk_cli.py --enable --opponent "NoobMaster69" --category gaming --intensity savage
  python trash_talk_cli.py --status
  python trash_talk_cli.py --demo
  python trash_talk_cli.py --roast
"""

import argparse
import json
from trash_talk import trash_talk_manager, TrashTalkCategory, IntensityLevel

def main():
    parser = argparse.ArgumentParser(description='Trash Talk Feature CLI')
    
    # Main actions
    parser.add_argument('--enable', action='store_true', help='Enable trash talk mode')
    parser.add_argument('--disable', action='store_true', help='Disable trash talk mode')
    parser.add_argument('--toggle', action='store_true', help='Toggle trash talk mode')
    parser.add_argument('--status', action='store_true', help='Show current status')
    parser.add_argument('--demo', action='store_true', help='Run demonstration')
    parser.add_argument('--roast', action='store_true', help='Generate a single roast')
    
    # Configuration options
    parser.add_argument('--opponent', type=str, help='Set opponent name')
    parser.add_argument('--category', choices=[c.value for c in TrashTalkCategory], 
                       help='Set trash talk category')
    parser.add_argument('--intensity', choices=[i.value for i in IntensityLevel], 
                       help='Set intensity level')
    
    # Context-specific roasts
    parser.add_argument('--intro', action='store_true', help='Generate intro roast')
    parser.add_argument('--victory', action='store_true', help='Generate victory taunt')
    
    # Export/Import
    parser.add_argument('--export', type=str, help='Export config to file')
    parser.add_argument('--import', dest='import_file', type=str, help='Import config from file')
    
    args = parser.parse_args()
    
    # Handle configuration changes first
    if args.opponent:
        trash_talk_manager.set_opponent(args.opponent)
        print(f"🎯 Opponent set to: {args.opponent}")
    
    if args.category:
        category = TrashTalkCategory(args.category)
        trash_talk_manager.set_category(category)
        print(f"📂 Category set to: {args.category.title()}")
    
    if args.intensity:
        intensity = IntensityLevel(args.intensity)
        trash_talk_manager.set_intensity(intensity)
        print(f"💥 Intensity set to: {args.intensity.title()}")
    
    # Handle main actions
    if args.enable:
        trash_talk_manager.toggle_trash_talk(True)
        print("🔥 TRASH TALK ENABLED! Let the roasting begin!")
    
    elif args.disable:
        trash_talk_manager.toggle_trash_talk(False)
        print("🔕 Trash talk disabled. Back to boring mode.")
    
    elif args.toggle:
        new_state = trash_talk_manager.toggle_trash_talk()
        status = "ENABLED 🔥" if new_state else "DISABLED 🔕"
        print(f"Trash talk toggled: {status}")
    
    elif args.status:
        print(trash_talk_manager.get_status())
    
    elif args.demo:
        from trash_talk import demo_trash_talk
        demo_trash_talk()
    
    elif args.roast:
        if trash_talk_manager.config.enabled:
            roast = trash_talk_manager.get_trash_talk()
            print(f"🔥 {roast}")
        else:
            print("🔕 Trash talk is disabled. Enable it first with --enable")
    
    elif args.intro:
        if trash_talk_manager.config.enabled:
            intro = trash_talk_manager.get_trash_talk('intro')
            print(f"🎬 {intro}")
        else:
            print("🔕 Trash talk is disabled. Enable it first with --enable")
    
    elif args.victory:
        if trash_talk_manager.config.enabled:
            victory = trash_talk_manager.get_trash_talk('victory')
            print(f"🏆 {victory}")
        else:
            print("🔕 Trash talk is disabled. Enable it first with --enable")
    
    elif args.export:
        config_data = trash_talk_manager.config.to_dict()
        with open(args.export, 'w') as f:
            json.dump(config_data, f, indent=2)
        print(f"💾 Configuration exported to {args.export}")
    
    elif args.import_file:
        try:
            with open(args.import_file, 'r') as f:
                config_data = json.load(f)
            trash_talk_manager.config.from_dict(config_data)
            print(f"📥 Configuration imported from {args.import_file}")
            print(trash_talk_manager.get_status())
        except FileNotFoundError:
            print(f"❌ Config file {args.import_file} not found")
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON in {args.import_file}")
    
    else:
        # No specific action, show help
        parser.print_help()

if __name__ == "__main__":
    main()
