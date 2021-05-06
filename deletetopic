from google.cloud import pubsub_v1

# TODO(developer)
# project_id = "your-project-id"
# topic_id = "your-topic-id"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

publisher.delete_topic(request={"topic": topic_path})

print("Topic deleted: {}".format(topic_path))
