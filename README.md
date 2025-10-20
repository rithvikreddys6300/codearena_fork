# CodeWars - LLM Battle Platform with Trash Talk Feature 🔥

An interactive platform where AI language models compete in coding challenges, now enhanced with a hilarious trash talk feature that adds competitive banter to the battles!

## Features

### Core Platform
- **Real-time LLM Battles**: Watch different AI models compete in coding challenges
- **Interactive Voting**: Vote on which model performed better
- **Leaderboard**: Track model performance over time
- **Live Code Preview**: See generated code running in real-time

### 🔥 NEW: Trash Talk Feature
- **Toggle On/Off**: Easy enable/disable functionality
- **Opponent Configuration**: Set custom opponent names
- **Multiple Categories**: Gaming, Sports, Programming, Academic, Cooking, General
- **Intensity Levels**: Mild (friendly), Medium (spicy), Savage (no mercy)
- **Context-Aware**: Different roasts for intros, mid-conversation, and victories
- **AI Integration**: Modifies AI prompts to include trash talk personality

## Quick Start

This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/create-next-app).

### Prerequisites

- Node.js 18+ 
- npm or pnpm
- Together AI API key

### Installation

```bash
# Clone the repository
git clone [your-repo-url]
cd codewars

# Install dependencies
npm install
# or
pnpm install

# Set up environment variables
cp .env.example .env.local
# Add your Together AI API key to .env.local
```

### Running the Development Server

```bash
npm run dev
# or
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Trash Talk Usage

### Basic UI Controls

1. **Enable Trash Talk**: Toggle the "🔥 Trash Talk Mode" switch on the main page
2. **Set Opponent**: Enter your opponent's name in the text field
3. **Choose Category**: Select from Gaming, Programming, Sports, Academic, Cooking, or General
4. **Pick Intensity**: Choose Mild, Medium, or Savage level roasts
5. **Generate Roasts**: Click "Generate Roast 💀" to see trash talk in action

### API Usage

The trash talk feature is accessible via REST API:

```typescript
// Enable trash talk
await fetch('/api/trash-talk', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    action: 'toggle',
    enabled: true
  })
});

// Set opponent
await fetch('/api/trash-talk', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    action: 'setOpponent',
    opponent: 'CodeNewbie'
  })
});

// Generate a roast
await fetch('/api/trash-talk', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    action: 'generateRoast',
    context: 'victory' // 'intro', 'mid', or 'victory'
  })
});
```

### TypeScript Integration

```typescript
import { trashTalkManager } from '@/lib/trash-talk';
import { TrashTalkCategory, IntensityLevel } from '@/types/trash-talk';

// Configure trash talk
trashTalkManager.toggleTrashTalk(true);
trashTalkManager.setOpponent('Opponent');
trashTalkManager.setCategory(TrashTalkCategory.PROGRAMMING);
trashTalkManager.setIntensity(IntensityLevel.SAVAGE);

// Generate roasts
const roast = trashTalkManager.getTrashTalk('victory');
console.log(roast); // "Opponent's code is so bad, even the compiler needs therapy"

// Modify AI prompts
const enhancedPrompt = trashTalkManager.modifyPrompt('You are a helpful AI assistant.');
```

## Tech Stack

- **Framework**: Next.js 15 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: Radix UI
- **Database**: PostgreSQL with Drizzle ORM
- **AI Integration**: Together AI
- **Code Sandbox**: Sandpack
- **Deployment**: Vercel

## Project Structure

```
src/
├── app/                    # Next.js app router
│   ├── api/               # API routes
│   │   ├── generate-app/  # Code generation endpoint
│   │   └── trash-talk/    # Trash talk API
│   ├── page.tsx           # Main battle page
│   └── layout.tsx         # Root layout
├── components/            # React components
│   ├── trash-talk/        # Trash talk components
│   │   ├── TrashTalkControls.tsx
│   │   └── TrashTalkDisplay.tsx
│   └── ui/               # Shared UI components
├── lib/                  # Utility functions
│   └── trash-talk.ts     # Trash talk core logic
└── types/               # TypeScript type definitions
    └── trash-talk.ts    # Trash talk interfaces
```

## Trash Talk Examples

### 🎮 Gaming Roasts
- **Mild**: "looks like {opponent} still uses Internet Explorer to download Chrome"
- **Savage**: "{opponent}'s gameplay is so bad, lag switches refuse to help them"

### 💻 Programming Burns
- **Mild**: "{opponent} writes code like they're playing Scrabble with missing tiles" 
- **Savage**: "If {opponent} wrote the code for a toaster, it would somehow catch fire while making ice"

### 🏆 Victory Celebrations
- "GG EZ! {opponent} brought a spoon to a knife fight and I brought a laser cannon! ⚡"
- "Flawless Victory! {opponent}, you can pick up your dignity at the lost and found... oh wait, they don't have it either! 👑"

## Environment Variables

Create a `.env.local` file with:

```env
TOGETHER_AI_API_KEY=your_together_ai_api_key_here
DATABASE_URL=your_postgresql_connection_string
HELICONE_API_KEY=your_helicone_key_for_monitoring (optional)
```

## Development

```bash
# Run the development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Lint code
npm run lint

# Database operations
npm run db:push    # Push schema changes
npm run db:pull    # Pull schema from database  
npm run db:studio  # Open database studio
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Remember**: The trash talk feature is all about having fun! Keep the roasting playful and enjoy the competitive banter! 🔥😎

## Learn More

To learn more about the technologies used:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API
- [Together AI](https://together.ai/) - AI model platform
- [Tailwind CSS](https://tailwindcss.com/) - utility-first CSS framework
- [TypeScript](https://www.typescriptlang.org/) - typed JavaScript

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.
