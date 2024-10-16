from flask import Flask, request, render_template
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        yt = YouTube(url)
        yt.streams.first().download()  # 첫 번째 스트림 다운로드
        return f'Downloaded: {yt.title}'
    return '''
        <form method="post">
            YouTube URL: <input type="text" name="url">
            <input type="submit" value="Download">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
