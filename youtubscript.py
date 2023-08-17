import os
from googleapiclient.discovery import build

# Set up the API client
API_KEY = 'YOUR_API_KEY'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

def get_transcript(video_id):
    request = youtube.captions().list(
        part="snippet",
        videoId=video_id
    )
    response = request.execute()
    
    if not response['items']:
        return None

    # Here, we're selecting the first available caption track.
    # You might want to iterate over 'items' and select based on the 'language' attribute.
    caption_id = response['items'][0]['id']
    
    # Download the transcript
    caption_request = youtube.captions().download(
        id=caption_id
    )
    caption_response = caption_request.execute()
    
    return caption_response.decode('utf-8')

video_id = "YOUR_VIDEO_ID"
transcript = get_transcript(video_id)
if transcript:
    print(transcript)
else:
    print("No transcript available for this video.")

