export type TeamType = 'product' | 'finance' | 'marketing';

export interface Stage {
  label: string;
  content: string;
}

export interface Pipeline {
  stages: Stage[];
}

export interface Pipelines {
  [key: string]: Pipeline;
}

export interface ChartDataPoint {
  date: string;
  value: number;
}

export interface ChartData {
  [key: string]: ChartDataPoint[];
}
