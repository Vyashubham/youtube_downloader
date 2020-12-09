from pytube import YouTube

link = input("link of the video you want to download: ")

yt_obj = YouTube(link)

#Title of video 
print('Title:', yt_obj.title)

#Number of views
print('Views:', yt_obj.views)

#Video Description
print('Description:', yt_obj.description)

#Length of video 
print('Length(in seconds):', yt_obj.length)

#Rating
print('Rating:', int(yt_obj.rating))

#Link
print('Link:', link)

download_request = input('do you want to download the video? [Y/N]')

#Download the video 
if download_request == "Y":

	video_download = yt_obj.streams.get_highest_resolution()
	video_download.download() #add location inside download to save to a different location

else:
	print("oh, okay.")


