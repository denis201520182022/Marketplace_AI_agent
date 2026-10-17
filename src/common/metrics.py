from prometheus_client import Counter, Histogram, Gauge

# Reviews & Inbound Events Counters
REVIEWS_PROCESSED_TOTAL = Counter(
    "marketplace_reviews_processed_total",
    "Total count of processed marketplace reviews and questions",
    ["platform", "event_type", "status"],
)

# LLM Performance
LLM_REQUEST_DURATION_SECONDS = Histogram(
    "llm_request_duration_seconds",
    "Duration of LLM inference requests in seconds",
    ["model_name"],
    buckets=[0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0],
)

LLM_TOKENS_TOTAL = Counter(
    "llm_tokens_total",
    "Total LLM tokens consumed",
    ["model_name", "type"],  # type: prompt / completion
)

# RabbitMQ Queues
RABBITMQ_QUEUE_DEPTH = Gauge(
    "rabbitmq_queue_depth",
    "Current message depth in RabbitMQ queues",
    ["queue_name"],
)

# Active Sellers
SELLER_ACTIVE_COUNT = Gauge(
    "seller_active_count",
    "Number of active sellers configured in the system",
    ["platform"],
)

# System Health
HEALTH_CHECK_STATUS = Gauge(
    "service_health_status",
    "Health status of subservices (1 = healthy, 0 = degraded)",
    ["subsystem"],
)
