from google.cloud import pubsub_v1

# TODO(developer)
# project_id = "your-project-id"
# topic_id = "your-topic-id"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

response = publisher.list_topic_subscriptions(request={"topic": topic_path})
for subscription in response:
    print(subscription)
