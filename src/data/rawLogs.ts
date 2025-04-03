// This file contains mock raw telemetry data that would typically come from a database
// In a real application, this would be fetched from an API

export const rawLogs = {
  product: [
    { user_id: "user1", event_type: "feature_use", timestamp: "2025-03-01T10:15:30Z" },
    { user_id: "user2", event_type: "feature_use", timestamp: "2025-03-02T11:20:45Z" },
    { user_id: "user3", event_type: "login", timestamp: "2025-03-03T09:30:15Z" },
    { user_id: "user1", event_type: "feature_use", timestamp: "2025-03-05T14:25:10Z" },
    { user_id: "user4", event_type: "feature_use", timestamp: "2025-03-10T16:40:20Z" }
  ],
  finance: [
    { user_id: "user1", billing_event: "subscription", charge_amount: 29.99, timestamp: "2025-03-01T00:00:00Z" },
    { user_id: "user2", billing_event: "one_time", charge_amount: 49.99, timestamp: "2025-03-03T00:00:00Z" },
    { user_id: "user3", billing_event: "subscription", charge_amount: 0, timestamp: "2025-03-05T00:00:00Z" }, // Free tier
    { user_id: "user4", billing_event: "subscription", charge_amount: 99.99, timestamp: "2025-03-07T00:00:00Z" },
    { user_id: "user5", billing_event: "one_time", charge_amount: 19.99, timestamp: "2025-03-15T00:00:00Z" }
  ],
  marketing: [
    { user_id: "user1", campaign_id: "spring_promo", event_type: "click", timestamp: "2025-03-02T08:15:30Z" },
    { user_id: "user2", campaign_id: "new_feature", event_type: "open", timestamp: "2025-03-04T09:20:45Z" },
    { user_id: "user3", campaign_id: "spring_promo", event_type: "ignore", timestamp: "2025-03-06T10:30:15Z" },
    { user_id: "user4", campaign_id: "new_feature", event_type: "click", timestamp: "2025-03-08T11:25:10Z" },
    { user_id: "user5", campaign_id: "discount", event_type: "open", timestamp: "2025-03-10T12:40:20Z" }
  ]
};
