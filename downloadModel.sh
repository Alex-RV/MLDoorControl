#!/bin/bash

# Function to download a file from Google Drive
download_file() {
    file_id="$1"  # Google Drive file ID
    destination="$2"  # Destination path to save the downloaded file

    # Construct the download URL
    url="https://drive.google.com/file/d/1TzeHoICU_37L1LnN_gYi9jR2KbnljT2l/view?usp=sharing"

    # Use curl to download the file
    curl -L -o "/trainer" "${url}"
}

# Example usage: download_file "<file_id>" "<destination_path>"

# Replace <file_id> with the actual file ID from Google Drive
# Replace <destination_path> with the desired destination path to save the downloaded file

