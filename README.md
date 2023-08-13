# YouTube-Downloader V0.0.0.1

This was made by using Python 3.11 and Vue JS

Note that this projects is at it's baby form for now, so expect many bugs and unfinished features.
Also take note that YouTube as far as I know does not allow any external downloads on the video hosted on the platform without the "download" button present. So keep that in mind. This is purely built for educational purposes.

# TODO
1. create loading screen when pressing download (currently there is no frontend indicator that tells that the download is done or an error has occured) 
2. get youtube video information
3. display youtube info in the download section (the thumbnail for now)
4. add options for download (i.e., mp4, mp3, wav, etc.,)

# BACKLOG
1. polish up the python api (it's in the "if it works, it works" stage for now)
2. display youtube description in the download section page, the description, and quality downloadable
3. polish ui/ux design
4. some ease of life features

# What is included in the python file?
1. Flask to create the api
2. Pytube to get the YouTube module (so we can download the videos)
3. re for regex functionality
4. os and glob for purging the downloads in the current working directory

# What is included in Vue JS?
1. Axios this is where we call our python api

# Usage
## Python Api
1. Make sure python 3.10 or greater is installed in your system
2. Run the Python file inside the api folder (i.e., ./python downloader_restful_api.py)

## Vue JS
1. cd into the youtube_downloader folder
2. npm install
3. npm run dev
4. open the link generated by vue js in your browser or wherever
5. the rest is straight forward, it has a UI interface

# UI Preview
![image](https://github.com/mosnamarco/YouTube-Downloader/assets/122838600/c36a28f6-7767-4ba3-b1e6-2f8041ba5180)
