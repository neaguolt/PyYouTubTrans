import googleapiclient.discovery

def get_transcript(api_key, video_id):
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
    
    # Solicitarea directă pentru a obține transcriptul
    request = youtube.captions().download(id=video_id)
    response = request.execute()
    
    return response

api_key = 'AIzaSyASniereNkEnzvJ3m64es4qKEYTsyDHr2Q'
video_id = '52nqjrCs57s'
transcript = get_transcript(api_key, video_id)
if transcript:
    with open(f'{video_id}_transcript.txt', 'w', encoding='utf-8') as file:
        file.write(transcript)
    print(f"Transcriptul a fost salvat ca {video_id}_transcript.txt.")
else:
    print("Nu există un transcript disponibil pentru acest videoclip.")

