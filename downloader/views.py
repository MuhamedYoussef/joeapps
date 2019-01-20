from django.shortcuts import render
from pytube import YouTube


def downloader(request):
    video = request.GET.get('video')
    videos = []

    if video:
        try:
            yt = YouTube(video)
            videos = yt.streams.filter(
                progressive=True, file_extension='mp4').order_by('resolution').all()
        except:
            pass

        if len(videos) != 0:

            for vid in videos:
                vid.size = int(vid.filesize / 1000000)

            context = {
                'url': video,
                'title': yt.title,
                'img': yt.thumbnail_url,
                'videos': videos
            }

            return render(request, 'downloader/downloader.html', context)
        else:
            context = {
                'err': 'No video matched, Check out your URL'
            }
            return render(request, 'downloader/downloader.html', context)

    return render(request, 'downloader/downloader.html')
