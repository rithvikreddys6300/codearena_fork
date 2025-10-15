"use client";

import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { TrashTalkCategory, IntensityLevel, TrashTalkStatus } from "@/types/trash-talk";

interface TrashTalkControlsProps {
  onTrashTalkChange?: (enabled: boolean) => void;
}

export default function TrashTalkControls({ onTrashTalkChange }: TrashTalkControlsProps) {
  const [status, setStatus] = useState<TrashTalkStatus | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  // Load initial status
  useEffect(() => {
    loadStatus();
  }, []);

  const loadStatus = async () => {
    try {
      const response = await fetch("/api/trash-talk");
      if (response.ok) {
        const data = await response.json();
        setStatus(data);
      }
    } catch (error) {
      console.error("Failed to load trash talk status:", error);
    }
  };

  const apiCall = async (action: string, params: Record<string, unknown> = {}) => {
    setIsLoading(true);
    try {
      const response = await fetch("/api/trash-talk", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action, ...params }),
      });

      if (response.ok) {
        await loadStatus(); // Reload status after any change
        return await response.json();
      }
    } catch (error) {
      console.error(`Failed to ${action}:`, error);
    } finally {
      setIsLoading(false);
    }
  };

  const toggleTrashTalk = async () => {
    const newEnabled = !status?.enabled;
    const result = await apiCall("toggle", { enabled: newEnabled });
    if (result && onTrashTalkChange) {
      onTrashTalkChange(newEnabled);
    }
  };

  const setOpponent = async (opponent: string) => {
    await apiCall("setOpponent", { opponent });
  };

  const setCategory = async (category: TrashTalkCategory) => {
    await apiCall("setCategory", { category });
  };

  const setIntensity = async (intensity: IntensityLevel) => {
    await apiCall("setIntensity", { intensity });
  };

  const generateRoast = async () => {
    const result = await apiCall("generateRoast", { context: "mid" });
    if (result?.roast) {
      alert(result.roast); // Simple display for now
    }
  };

  if (!status) {
    return <div className="text-sm text-gray-500">Loading trash talk...</div>;
  }

  return (
    <div className="space-y-4 rounded-lg border border-red-200 bg-red-50 p-4">
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-bold text-red-700">🔥 Trash Talk Mode</h3>
        <Button
          onClick={toggleTrashTalk}
          disabled={isLoading}
          variant={status.enabled ? "destructive" : "outline"}
          size="sm"
        >
          {status.enabled ? "Disable" : "Enable"}
        </Button>
      </div>

      {status.enabled && (
        <div className="space-y-3">
          {/* Opponent Input */}
          <div>
            <label className="block text-sm font-medium text-red-700 mb-1">
              Opponent Name
            </label>
            <input
              type="text"
              value={status.opponent}
              onChange={(e) => setOpponent(e.target.value)}
              className="w-full rounded border border-red-300 px-2 py-1 text-sm"
              placeholder="Enter opponent name"
            />
          </div>

          {/* Category Selector */}
          <div>
            <label className="block text-sm font-medium text-red-700 mb-1">
              Category
            </label>
            <select
              value={status.category}
              onChange={(e) => setCategory(e.target.value as TrashTalkCategory)}
              className="w-full rounded border border-red-300 px-2 py-1 text-sm"
            >
              {Object.values(TrashTalkCategory).map((category) => (
                <option key={category} value={category}>
                  {category.charAt(0).toUpperCase() + category.slice(1)}
                </option>
              ))}
            </select>
          </div>

          {/* Intensity Selector */}
          <div>
            <label className="block text-sm font-medium text-red-700 mb-1">
              Intensity
            </label>
            <select
              value={status.intensity}
              onChange={(e) => setIntensity(e.target.value as IntensityLevel)}
              className="w-full rounded border border-red-300 px-2 py-1 text-sm"
            >
              {Object.values(IntensityLevel).map((intensity) => (
                <option key={intensity} value={intensity}>
                  {intensity.charAt(0).toUpperCase() + intensity.slice(1)}
                </option>
              ))}
            </select>
          </div>

          {/* Generate Roast Button */}
          <div className="flex gap-2">
            <Button
              onClick={generateRoast}
              disabled={isLoading}
              variant="outline"
              size="sm"
              className="border-red-300 text-red-700 hover:bg-red-100"
            >
              Generate Roast 💀
            </Button>
          </div>

          {/* Status Display */}
          {status.roastCount > 0 && (
            <div className="text-xs text-red-600">
              Roasts delivered: {status.roastCount}
              {status.lastRoast && (
                <div className="mt-1 italic">&quot;{status.lastRoast}&quot;</div>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
