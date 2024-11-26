from google.cloud import pubsub_v1
import time

# Configuration: specify your Google Cloud project ID and Pub/Sub topic ID
project_id = "qwiklabs-gcp-00-71c335c5bd23"  # Replace with your project ID
topic_id = "receive_data"  # Replace with your topic ID

# Create a Publisher client
publisher = pubsub_v1.PublisherClient()

# Build the fully qualified topic path
topic_path = publisher.topic_path(project_id, topic_id)

# Publish messages to the topic
for n in range(1, 10):  # Adjust range as needed
    data_str = f"Message number {n}"  # Message to publish
    data = data_str.encode("utf-8")  # Convert to byte string
    print(f"Publishing: {data_str}")
    
    # Publish the message
    future = publisher.publish(topic_path, data)
    
    # Block until the message is published and print result
    print(future.result())
    
    # Pause between messages
    time.sleep(1)

print(f"Published messages to {topic_path}.")
