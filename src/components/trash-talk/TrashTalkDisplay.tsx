"use client";

import { useState, useEffect } from "react";

interface TrashTalkDisplayProps {
  context?: "intro" | "mid" | "victory";
  autoShow?: boolean;
}

export default function TrashTalkDisplay({ context = "mid", autoShow = false }: TrashTalkDisplayProps) {
  const [roast, setRoast] = useState<string>("");
  const [isVisible, setIsVisible] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const checkAndShowRoast = async () => {
    try {
      // First check if trash talk is enabled
      const statusResponse = await fetch("/api/trash-talk");
      if (!statusResponse.ok) return;
      
      const status = await statusResponse.json();
      if (!status.enabled) return;

      // Generate a roast
      const roastResponse = await fetch("/api/trash-talk", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "generateRoast", context }),
      });

      if (roastResponse.ok) {
        const data = await roastResponse.json();
        if (data.roast) {
          setRoast(data.roast);
          setIsVisible(true);
          
          // Auto-hide after 5 seconds
          setTimeout(() => {
            setIsVisible(false);
          }, 5000);
        }
      }
    } catch (error) {
      console.error("Failed to generate trash talk:", error);
    }
  };

  useEffect(() => {
    if (autoShow) {
      checkAndShowRoast();
    }
  }, [autoShow, context]);

  const generateRoast = async () => {
    setIsLoading(true);
    try {
      const response = await fetch("/api/trash-talk", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "generateRoast", context }),
      });

      if (response.ok) {
        const data = await response.json();
        if (data.roast) {
          setRoast(data.roast);
          setIsVisible(true);
        }
      }
    } catch (error) {
      console.error("Failed to generate roast:", error);
    } finally {
      setIsLoading(false);
    }
  };

  if (!isVisible && !autoShow) return null;

  return (
    <div className={`transition-all duration-500 ${isVisible ? "opacity-100 scale-100" : "opacity-0 scale-95"}`}>
      {roast && (
        <div className="mb-4 rounded-lg border-2 border-red-400 bg-gradient-to-r from-red-100 to-orange-100 p-4 shadow-lg">
          <div className="flex items-start justify-between">
            <div className="flex-1">
              <div className="flex items-center gap-2 mb-2">
                <span className="text-lg">🔥</span>
                <span className="font-bold text-red-700 text-sm uppercase tracking-wide">
                  Trash Talk Activated
                </span>
              </div>
              <p className="text-red-800 font-medium italic">
                &quot;{roast}&quot;
              </p>
            </div>
            <button
              onClick={() => setIsVisible(false)}
              className="ml-2 text-red-400 hover:text-red-600 text-xl leading-none"
            >
              ×
            </button>
          </div>
        </div>
      )}
      
      {!autoShow && (
        <div className="text-center mb-4">
          <button
            onClick={generateRoast}
            disabled={isLoading}
            className="rounded bg-red-600 px-4 py-2 text-white hover:bg-red-700 disabled:opacity-50"
          >
            {isLoading ? "Generating..." : "🔥 Trash Talk"}
          </button>
        </div>
      )}
    </div>
  );
}
