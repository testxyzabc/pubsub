from google.cloud import pubsub_v1

# TODO(developer)
# project_id = "your-project-id"
# subscription_id = "your-subscription-id"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

# Wrap the subscriber in a 'with' block to automatically call close() to
# close the underlying gRPC channel when done.
with subscriber:
    subscriber.delete_subscription(request={"subscription": subscription_path})

print(f"Subscription deleted: {subscription_path}.")
