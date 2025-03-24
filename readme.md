Markdown

# Discord Neko Bot - Enhanced Readme

This is a simple yet fun Discord bot that responds to the `neko` command by sending adorable cat images. It's built with Python and leverages the Discord.py library for Discord interactions and the requests library for fetching images from the Cat API.

## Detailed Features

-   **`neko` Command:**
    -      Responds to the `neko` command, regardless of capitalization
    -      Fetches a random cat image from the Cat API.
    -      Handles API errors gracefully, providing a user-friendly message if image retrieval fails.
-   **Environment Variable Security:**
    -      Uses a `.env` file to store the Discord bot token, ensuring sensitive information is not hardcoded into the script.
    -      Leverages the `python-dotenv` library to load environment variables.
     **Discord Intents:**
    -   Properly sets up discord intents to make sure that the bot can read message content.

