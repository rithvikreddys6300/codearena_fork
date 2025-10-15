import { NextRequest, NextResponse } from "next/server";
import { trashTalkManager } from "@/lib/trash-talk";
import { TrashTalkCategory, IntensityLevel } from "@/types/trash-talk";

export async function GET() {
  try {
    const status = trashTalkManager.getStatus();
    return NextResponse.json(status);
  } catch (error) {
    console.error("Error getting trash talk status:", error);
    return NextResponse.json(
      { error: "Failed to get trash talk status" },
      { status: 500 }
    );
  }
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { action, ...params } = body;

    switch (action) {
      case "toggle":
        const enabled = trashTalkManager.toggleTrashTalk(params.enabled);
        return NextResponse.json({ enabled });

      case "setOpponent":
        trashTalkManager.setOpponent(params.opponent);
        return NextResponse.json({ success: true });

      case "setCategory":
        if (Object.values(TrashTalkCategory).includes(params.category)) {
          trashTalkManager.setCategory(params.category);
          return NextResponse.json({ success: true });
        }
        return NextResponse.json(
          { error: "Invalid category" },
          { status: 400 }
        );

      case "setIntensity":
        if (Object.values(IntensityLevel).includes(params.intensity)) {
          trashTalkManager.setIntensity(params.intensity);
          return NextResponse.json({ success: true });
        }
        return NextResponse.json(
          { error: "Invalid intensity" },
          { status: 400 }
        );

      case "generateRoast":
        const roast = trashTalkManager.getTrashTalk(params.context);
        return NextResponse.json({ roast });

      case "modifyPrompt":
        const modifiedPrompt = trashTalkManager.modifyPrompt(params.basePrompt);
        return NextResponse.json({ modifiedPrompt });

      case "updateConfig":
        trashTalkManager.updateConfig(params.config);
        return NextResponse.json({ success: true });

      case "reset":
        trashTalkManager.reset();
        return NextResponse.json({ success: true });

      case "exportConfig":
        const configJson = trashTalkManager.exportConfig();
        return NextResponse.json({ config: configJson });

      case "importConfig":
        const importSuccess = trashTalkManager.importConfig(params.configJson);
        return NextResponse.json({ success: importSuccess });

      default:
        return NextResponse.json(
          { error: "Invalid action" },
          { status: 400 }
        );
    }
  } catch (error) {
    console.error("Error in trash talk API:", error);
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 }
    );
  }
}
