import yt_dlp

# type the url of the video that you want to download
url = "https://www.youtube.com/watch?v=GbHcePUTszk&t=147s"

ydl_opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
    "outtmpl": "C:/intern/pythonProjects/pythonProject/python_assignment/videos/%(title)s.%(ext)s",
    "merge_output_format": "mp4"  # ensure the final file is in .mp4 format
}

ydl = yt_dlp.YoutubeDL(ydl_opts)
ydl.download([url])
