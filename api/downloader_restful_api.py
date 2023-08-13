#call as: http://localhost:port/download/?url=<url link here> 
#TODO: Create Filter for youtube link [done (regex)]
#TODO: Fix Download (Not sure if it prompts users to accept download file) [done]
#TODO: Return errors if needed [done (needs improvement)]
#TODO: Return json file containing video info [done]

from flask import Flask, request, send_file, jsonify
from pytube import YouTube
from pytube.helpers import safe_filename
import re, os, glob

app = Flask(__name__)

@app.route("/download/")
def api_cors():
    url = request.args.get('url')

    regex = r"^(https?\:\/\/)?((www\.)?youtube\.com|youtu\.be)\/.+$"
    if re.match(regex, url):
        video = YouTube(url)
        name = (safe_filename(video.title) + ".mp4")
        video_stream = video.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        video_stream.download()
        return send_file(name, as_attachment=True, download_name=video.title + '.mp4')
    else:
        error_message = [{"error_message": "invalid url", "msg": "Enter Correct Link"}]
        return jsonify(error_message)

#probably a security issue
@app.route("/purge")
def purge():
    downloaded_list = glob.glob('*.mp4')
    for f in downloaded_list:
        os.remove(f)
    return ('purged...', 204)

if __name__ == "__main__":
    app.run(debug=True)