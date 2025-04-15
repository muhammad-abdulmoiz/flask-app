# Flask Weather Application

A simple Flask application to fetch and manage weather data.

## Features

1. **Get Current Weather**
   - Returns current weather based on given **latitude and longitude**.

2. **Retrieve Weather History**
   - Returns previously fetched weather data stored in memory.
   - Maintains a list of recent queries and their results.
   - The list can be limited to the last N items.

3. **Clear Weather History**
   - Provides an option to clear the in-memory weather history.

4. **Support for Location-Based Weather**
   - Supports fetching weather data by coordinates (latitude and longitude).