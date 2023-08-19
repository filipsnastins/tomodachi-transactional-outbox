resource "aws_dynamodb_table" "default" {
  name             = "${var.environment}-${var.aggregate_name}-outbox"
  billing_mode     = "PAY_PER_REQUEST"
  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"

  hash_key = "PK"

  point_in_time_recovery {
    enabled = true
  }

  server_side_encryption {
    enabled = true
  }

  attribute {
    name = "PK"
    type = "S"
  }

  attribute {
    name = "CorrelationId"
    type = "S"
  }

  attribute {
    name = "AggregateId"
    type = "S"
  }

  attribute {
    name = "NotDispatched"
    type = "S"
  }

  global_secondary_index {
    name            = "CorrelationIdIndex"
    hash_key        = "CorrelationId"
    projection_type = "ALL"
  }

  global_secondary_index {
    name            = "AggregateIdIndex"
    hash_key        = "AggregateId"
    projection_type = "ALL"
  }

  global_secondary_index {
    name            = "NotDispatchedMessagesIndex"
    hash_key        = "NotDispatched"
    projection_type = "ALL"
  }
}
