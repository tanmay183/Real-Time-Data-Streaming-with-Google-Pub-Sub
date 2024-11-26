from google.cloud import pubsub_v1

# Configuration: project and subscription details
project_id = "qwiklabs-gcp-00-71c335c5bd23"  # Replace with your Google Cloud project ID
subscription_id = "receive_data-sub"     # Replace with your subscription ID
timeout = 5.0  # Number of seconds the subscriber should listen for messages

# Create a subscriber client
subscriber = pubsub_v1.SubscriberClient()

# Define the subscription path
subscription_path = subscriber.subscription_path(project_id, subscription_id)

# Callback function to process received messages
def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    print(f"Received message: {message.data.decode('utf-8')}")
    message.ack()  # Acknowledge the message

# Subscribe to the topic and listen for messages
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}...\n")

# Wrap subscriber in a try-except block to handle graceful shutdown
with subscriber:
    try:
        streaming_pull_future.result(timeout=timeout)
    except TimeoutError:
        streaming_pull_future.cancel()  # Cancel the streaming pull
        streaming_pull_future.result()  # Wait until the subscription is fully closed
