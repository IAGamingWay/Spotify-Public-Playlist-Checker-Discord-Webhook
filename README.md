# Spotify Public Playlist Checker
The Spotify Public Playlist Checker Discord Webhook is a simple tool that sends instant Discord notifications for changes in public Spotify playlists.

# What is this?
A Python script that monitors changes in public Spotify playlists and sends notifications to a Discord webhook when new playlists are detected. To use this script, you need to replace placeholder values with your actual Spotify client credentials, Discord webhook URL, and Spotify user ID.

1. **Create a Spotify App:**
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Log in with your Spotify account or create one if you don't have it.
   - Click on "Create an App" and fill in the required information.
   - After creating the app, you'll find your `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` on the app's dashboard.

2. **Get Spotify User ID:**
   - Open the Spotify desktop or mobile app.
   - Go to your profile by clicking on your name.
   - Click on the three dots (More) and choose "Copy Spotify URL."
   - Extract your user ID from the URL.

3. **Create a Discord Webhook:**
   - In your Discord server, right-click on the channel where you want the notifications and click on "Edit Channel."
   - Go to the "Webhooks" section and click on "Create Webhook."
   - Copy the webhook URL.

4. **Replace Placeholder Values:**
   - Replace `'your_client_id'` and `'your_client_secret'`.
   - Replace `'your_discord_webhook'` with the Discord webhook URL.
   - Replace `'your_profile_id'` with your target Spotify user ID.

Save the changes, and you can run the script.
