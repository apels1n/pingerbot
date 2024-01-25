####This telegram bot can help you monitor the network availability of important hosts. Or it can be used to check for power availability.

>The bot is deployed in a docker container, which allows you to have several different instances independent of each other, to check different network hosts, with a different set of custom phrases for each individual instance

##Configuration Steps:

1. Install Docker
2. Download and edit `compose.yaml` file. Enter the following information into it:
	- _token_ - bot API token
	- _chat_id_ - Channel or Chat _id_
	- _host_title_ - Host name
	- _host_ip_ - Host IP or domain name
	- _timeout_ - Host availability check frequency (**in seconds**)
	- _host_up_msg_ - The message you will receive in Telegram if the host becomes available
		>Example:
		```bash
		f"Host {host_title} ({host_ip}) is UP"
		```
	- _host_down_msg_ - The message you will receive in Telegram if the host becomes unavailable
		>Example:
		```bash
		f"Host {host_title} ({host_ip}) is DOWN"
		```

3. Deploy the docker container:
    ```bash
    docker compose up -d
    ```

##Example Screenshot

![Picture](https://i.ibb.co/nBh6cg8/photo-2024-01-25-21-57-04.jpg)
