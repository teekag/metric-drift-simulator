/**
 * Helper functions for the Metric Normalization Explorer
 */

/**
 * Formats a number for display (adds commas, fixed decimals)
 */
export const formatNumber = (num: number): string => {
  return num.toLocaleString('en-US');
};

/**
 * Calculates the percentage difference between two values
 */
export const calculateDifference = (value1: number, value2: number): number => {
  if (value2 === 0) return 0;
  return ((value1 - value2) / value2) * 100;
};

/**
 * Formats a percentage for display
 */
export const formatPercentage = (percentage: number): string => {
  const sign = percentage >= 0 ? '+' : '';
  return `${sign}${percentage.toFixed(1)}%`;
};

/**
 * Compares two team's metric definitions and returns key differences
 */
export const compareMetricDefinitions = (team1: string, team2: string): string => {
  const comparisons: Record<string, Record<string, string>> = {
    product: {
      finance: "Product tracks feature usage while Finance only counts paying customers.",
      marketing: "Product measures actual product usage while Marketing includes campaign interactions."
    },
    finance: {
      product: "Finance only counts paying users while Product includes all active users.",
      marketing: "Finance focuses on revenue-generating users while Marketing tracks campaign engagement."
    },
    marketing: {
      product: "Marketing includes campaign interactions while Product only counts actual feature usage.",
      finance: "Marketing includes all engaged users while Finance only counts paying customers."
    }
  };

  return comparisons[team1]?.[team2] || "No comparison available.";
};
