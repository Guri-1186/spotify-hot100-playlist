# Billboard Hot 100 Playlist Generator

This Python project generates a playlist on Spotify based on the Billboard Hot 100 chart for a given date. The user inputs a date (in the format `YYYY-MM-DD`), and the script fetches the song titles from the Billboard Hot 100 for that date, searches for them on Spotify, and creates a private playlist with the found songs.

## Features:

- Fetches the Billboard Hot 100 chart for a given date.
- Searches for the corresponding songs on Spotify.
- Creates a private playlist with the found songs on the user's Spotify account.
- Skips any songs not available on Spotify.

## Requirements:

1. Python 3.x
2. Spotipy library for Spotify API integration
3. Requests and BeautifulSoup libraries for web scraping
4. Python-dotenv for managing environment variables

## Installation:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/billboard-hot100-playlist.git
   cd billboard-hot100-playlist
   ```
