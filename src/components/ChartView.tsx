import React from 'react';
// Import Recharts components with type assertions to fix TypeScript errors
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, Legend, ResponsiveContainer } from 'recharts';
import { ChartDataPoint, TeamType } from '../types/types';

// Use type assertion to fix TypeScript errors with Recharts components
const RechartsComponents = {
  LineChart: LineChart as any,
  Line: Line as any,
  XAxis: XAxis as any,
  YAxis: YAxis as any,
  Tooltip: Tooltip as any,
  CartesianGrid: CartesianGrid as any,
  Legend: Legend as any,
  ResponsiveContainer: ResponsiveContainer as any
};

interface Props {
  data: ChartDataPoint[];
  selectedTeam: TeamType;
}

export const ChartView = ({ data, selectedTeam }: Props) => (
  <div className="bg-white p-4 rounded shadow">
    <h3 className="font-semibold text-blue-700 mb-4">Output of {selectedTeam.charAt(0).toUpperCase() + selectedTeam.slice(1)} MAU Over Time</h3>
    <div className="h-64">
      <RechartsComponents.ResponsiveContainer width="100%" height="100%">
        <RechartsComponents.LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <RechartsComponents.CartesianGrid strokeDasharray="3 3" />
          <RechartsComponents.XAxis dataKey="date" />
          <RechartsComponents.YAxis />
          <RechartsComponents.Tooltip />
          <RechartsComponents.Legend />
          <RechartsComponents.Line type="monotone" dataKey="value" stroke="#3b82f6" activeDot={{ r: 8 }} />
        </RechartsComponents.LineChart>
      </RechartsComponents.ResponsiveContainer>
    </div>
  </div>
);
