from pytube import YouTube
link = input("enter your fucking link")
print("Wait a minute bitch")
YouTube(link).streams.first().download()
print("Video Downloaded Motherfucker")
