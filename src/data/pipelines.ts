import { Pipelines } from '../types/types';

export const pipelines: Pipelines = {
  product: {
    stages: [
      { label: 'Raw Logs', content: 'user_id, event_type, timestamp' },
      {
        label: 'Transform',
        content: `SELECT DISTINCT user_id FROM logs WHERE event_type = 'feature_use' AND timestamp >= CURRENT_DATE - INTERVAL '30 days'`,
      },
      {
        label: 'Normalize',
        content: 'Monthly count of distinct users using product features',
      },
    ],
  },
  finance: {
    stages: [
      { label: 'Raw Logs', content: 'user_id, billing_event, timestamp' },
      {
        label: 'Transform',
        content: `SELECT DISTINCT user_id FROM billing WHERE charge_amount > 0`,
      },
      {
        label: 'Normalize',
        content: 'Monthly count of paying users',
      },
    ],
  },
  marketing: {
    stages: [
      { label: 'Raw Logs', content: 'user_id, campaign_id, event_type' },
      {
        label: 'Transform',
        content: `SELECT DISTINCT user_id FROM campaign_events WHERE event_type IN ('click', 'open')`,
      },
      {
        label: 'Normalize',
        content: 'Monthly count of users responding to campaigns',
      },
    ],
  },
};
