import React, { useState } from 'react';
import { TeamType } from '../types/types';

interface Props {
  selectedTeam: TeamType;
}

const explanations: Record<TeamType, string> = {
  product: `Product MAU focuses on users who interacted with specific features. It captures engagement but may miss users who log in but don't perform key actions.`,
  finance: `Finance MAU is derived from billing activity. It tracks paying users but ignores free-tier engagement or usage without purchases.`,
  marketing: `Marketing MAU includes users who responded to campaigns, such as clicks or opens. It's useful for campaign ROI but may inflate active user counts.`,
};

// Drift insights comparing each team's approach to others
type DriftInsightMap = {
  [key in TeamType]: {
    [key in TeamType]?: string;
  }
};

const driftInsights: DriftInsightMap = {
  product: {
    finance: "This differs from Finance MAU by filtering for product events, not billing events.",
    marketing: "Unlike Marketing MAU, Product MAU excludes campaign interactions that don't lead to product usage."
  },
  finance: {
    product: "Finance MAU differs from Product MAU by focusing only on paying users, ignoring free-tier engagement.",
    marketing: "Unlike Marketing MAU, Finance MAU only counts users with billing activity, not campaign interactions."
  },
  marketing: {
    product: "Marketing MAU includes campaign interactions that Product MAU would ignore if they don't lead to feature usage.",
    finance: "Unlike Finance MAU, Marketing MAU includes users who engage with campaigns but haven't made purchases."
  }
};

export const ExplanationPanel = ({ selectedTeam }: Props) => {
  // Using useState without generic type parameter to avoid TypeScript error
  const [comparisonTeam, setComparisonTeam] = useState(null as TeamType | null);
  
  // Get other teams for comparison
  const allTeams: TeamType[] = ['product', 'finance', 'marketing'];
  const otherTeams: TeamType[] = allTeams.filter(team => team !== selectedTeam);
  
  return (
    <div className="bg-white rounded-lg border p-4 shadow-sm">
      <h2 className="text-lg font-semibold text-gray-800 mb-2">
        Explanation: {selectedTeam.charAt(0).toUpperCase() + selectedTeam.slice(1)} MAU
      </h2>
      <p className="text-sm text-gray-700 leading-relaxed mb-4">
        {explanations[selectedTeam]}
      </p>
      
      {/* Drift Insight Section */}
      <div className="mt-4 pt-3 border-t border-gray-200">
        <h3 className="text-sm font-semibold text-gray-700 mb-2">Metric Drift Insights</h3>
        
        {comparisonTeam ? (
          <div className="bg-blue-50 p-3 rounded-md text-sm">
            <div className="flex justify-between items-center mb-2">
              <span className="font-medium">Comparing with {comparisonTeam.charAt(0).toUpperCase() + comparisonTeam.slice(1)} MAU</span>
              <button 
                onClick={() => setComparisonTeam(null)}
                className="text-xs text-blue-600 hover:text-blue-800"
              >
                Close
              </button>
            </div>
            <p className="text-gray-700">
              {comparisonTeam && 
               driftInsights[selectedTeam] && 
               comparisonTeam in driftInsights[selectedTeam] ? 
               driftInsights[selectedTeam][comparisonTeam as keyof typeof driftInsights[typeof selectedTeam]] : 
               "No comparison available."}
            </p>
          </div>
        ) : (
          <div className="flex flex-wrap gap-2">
            {otherTeams.map(team => (
              <button
                key={team}
                onClick={() => setComparisonTeam(team)}
                className="text-xs bg-gray-100 hover:bg-gray-200 text-gray-700 py-1 px-2 rounded-full"
              >
                Compare to {team.charAt(0).toUpperCase() + team.slice(1)}
              </button>
            ))}
          </div>
        )}
      </div>
      
      {/* Interactive Questions Section */}
      <div className="mt-4 pt-3 border-t border-gray-200">
        <h3 className="text-sm font-semibold text-gray-700 mb-2">Ask about this metric</h3>
        <div className="flex flex-wrap gap-2">
          <button className="text-xs bg-gray-100 hover:bg-gray-200 text-gray-700 py-1 px-2 rounded-full">
            Why is this important?
          </button>
          <button className="text-xs bg-gray-100 hover:bg-gray-200 text-gray-700 py-1 px-2 rounded-full">
            Show usage example
          </button>
          <button className="text-xs bg-gray-100 hover:bg-gray-200 text-gray-700 py-1 px-2 rounded-full">
            Copy SQL to clipboard
          </button>
        </div>
      </div>
    </div>
  );
};
