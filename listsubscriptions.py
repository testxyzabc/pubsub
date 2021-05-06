from google.cloud import pubsub_v1

# TODO(developer)
# project_id = "your-project-id"

subscriber = pubsub_v1.SubscriberClient()
project_path = f"projects/{project_id}"

# Wrap the subscriber in a 'with' block to automatically call close() to
# close the underlying gRPC channel when done.
with subscriber:
    for subscription in subscriber.list_subscriptions(
        request={"project": project_path}
    ):
        print(subscription.name)
