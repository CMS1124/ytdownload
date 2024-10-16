from flask import Flask, request, jsonify, send_file
import os
from pytube import YouTube

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    youtube_url = data.get('url')

    if not youtube_url:
        return jsonify({'success': False, 'error': 'No URL provided'})

    try:
        yt = YouTube(youtube_url)
        stream = yt.streams.get_highest_resolution()  # 가장 높은 해상도의 영상 다운로드
        download_path = stream.download()

        return jsonify({'success': True, 'downloadUrl': f'/files/{os.path.basename(download_path)}'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/files/<filename>')
def serve_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
