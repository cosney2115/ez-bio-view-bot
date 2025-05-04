# ez-bio-view-bot

A multi-threaded view bot designed for sending automated views to e-z.bio profiles using proxy rotation and random user-agent generation.

## Features

- **Multi-threaded Execution**: Send multiple views concurrently for maximum efficiency.
- **Proxy Support**: Automatically rotates through a list of proxies to avoid detection.
- **Random User-Agent Generation**: Mimics real browser behavior to reduce the risk of being flagged.
- **Simple Configuration**: Easy-to-use interface for quick setup and execution.

## How It Works

1. The bot reads a list of proxies from a `proxy.txt` file.
2. It generates random user-agent strings to simulate different devices and browsers.
3. Using multiple threads, it sends view requests to the specified e-z.bio profile.

## Requirements

- **Python 3.6+**
- Required Python packages:
  - `curl_cffi`
  - `loguru`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/cosney2115/ez-bio-view-bot.git
   cd ez-bio-view-bot
   ```

2. Install the required dependencies:

   ```bash
   pip install curl_cffi loguru
   ```

3. Prepare your proxy.txt file:
   - Add your proxies in the format `ip:port`, one per line.

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. Enter the username of the e-z.bio profile you want to send views to.

3. Specify the number of threads to use (e.g., 10 for 10 concurrent view requests).

## Example

```plaintext
Enter username: example_user
Enter number of threads: 10
```

The bot will start sending views to the specified profile using the provided number of threads.

## File Structure

```
ez-bio-view-bot/
├── main.py         # Main script for the bot
├── proxy.txt       # File containing the list of proxies
├── README.md       # Documentation
```

## Disclaimer

This tool is for educational purposes only. Using bots to artificially inflate view counts may violate e-z.bio's terms of service. Use this tool responsibly and at your own risk.

```

```
