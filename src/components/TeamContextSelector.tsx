import React from 'react';
import { TeamType } from '../types/types';

interface Props {
  selected: TeamType;
  setSelected: (team: TeamType) => void;
}

export const TeamContextSelector = ({ selected, setSelected }: Props) => {
  const teams: TeamType[] = ['product', 'finance', 'marketing'];

  return (
    <div className="flex space-x-2 mt-4">
      {teams.map((team) => (
        <button
          key={team}
          onClick={() => setSelected(team)}
          className={`px-4 py-2 rounded ${
            selected === team ? 'bg-blue-600 text-white' : 'bg-white border text-gray-700'
          }`}
        >
          {team.charAt(0).toUpperCase() + team.slice(1)}
        </button>
      ))}
    </div>
  );
};
