# Real-Time-Data-Streaming-with-Google-Pub-Sub

![image](https://github.com/user-attachments/assets/6b49f1a8-fdcc-4139-9a57-7c0f5a5347d7)


Search pub/sub

create topic recieve_data

check subscription created for it.

go to compute engine

click on create new instance name as publisher

choose nearest region

choose N1 series

in Access scopes

Enable cloud pub/sub

click on create

open in ssh


click on create new instance name as subscriber

choose nearest region

choose N1 series

in Access scopes

Enable cloud pub/sub

click on create

open in ssh

in publisher ssh :
sudo apt-get update

python3

sudo apt-get install python3-pip

sudo apt install python3-venv

python3 -m venv myenv

source myenv/bin/activate

pip install google-cloud-pubsub

ls -lrt

vi publisher.py

paste this code

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


in subscriber ssh :
sudo apt-get update

python3

sudo apt-get install python3-pip

sudo apt install python3-venv

python3 -m venv myenv

source myenv/bin/activate

pip install google-cloud-pubsub

paste below code

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


Run Publisher code :
python3 publisher.py


Run subscriber code :
python3 subscriber.py

# Publisher Execution

![producer](https://github.com/user-attachments/assets/7f223d2f-e1a2-4b58-9484-35592d89fb69)

# Subscriber Execution

![subscriber](https://github.com/user-attachments/assets/6b1280e8-47c6-434a-b873-2f6331c4fbf3)






