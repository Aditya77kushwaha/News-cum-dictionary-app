from django.shortcuts import render
import requests
import isodate

YOUTUBE_DATA_API = "AIzaSyB4a56W5l-cPP1PeW7r_TuJERoEG5scbQM"


def index(request):
    videos = []
    if request.method == "POST":
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'


        if request.POST['submit'] == 'news':
            x = "latest news"

        else :
            x = request.POST['search']
        search_params = {
            'part': 'snippet',
            'q': x,
            'key': YOUTUBE_DATA_API,
            'maxResults': 9,
            'type': 'video'
        }

        video_ids = []
        r = requests.get(search_url, params=search_params)

        results = r.json()['items']

        for result in results:
            video_ids.append(result['id']['videoId'])

        video_params = {
            'key': YOUTUBE_DATA_API,
            'part': 'snippet, contentDetails',
            'id': ','.join(video_ids),
            'maxResults' : 9
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()['items']

        
        for result in results :
            video_data = {
                'title' : result['snippet']['title'],
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'duration' : int(isodate.parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail' : result['snippet']['thumbnails']['high']['url'],
            }

            videos.append(video_data)

    return render(request, "index.html", {'videos' : videos})
