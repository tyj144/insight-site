from flask import Flask, render_template, Response, jsonify, request
from camera import VideoCamera
import json
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/formal')
def formal():
	return render_template('record.html', formal=True)

@app.route('/informal')
def informal():
	return render_template('record.html', formal=False)

@app.route('/results')
def results():
	text = get_text('static/text_folder/output_text.txt')
	stop_words = get_text('static/text_folder/output_stop.txt').split("\n")
	warning_words = get_text('static/text_folder/output_interested.txt').split("\n")
	synonyms = json.load(open('static/text_folder/my_synonym.json'))
	print(type(synonyms))

	for key, value in synonyms.items():
		synonyms[key] = value[:5]

	print(synonyms)
    
	return render_template('results.html', text=text.split(" "), stop_words=stop_words, warning_words=warning_words, synonyms=synonyms)

def get_text(filename):
	with open(filename, 'r') as f:
		text = f.read()

	return text

# @app.route('/record_status', methods=['POST'])
# def record_status():
# 	video_camera = None

# 	if video_camera == None:
# 		video_camera = VideoCamera

# 	json = request.json()

# 	status = json['status']

# 	if status == "true":
# 		video_camera.start_record()
# 		return jsonify(result="started")
# 	else:
# 		video_camera.stop_record()
# 		return jsonify(result="stopped")

# # http://www.codepool.biz/web-camera-recorder-oepncv-flask.html
# def video_stream():
# 	global video_camera
# 	global global_frame

# 	if video_camera == None:
# 		video_camera = VideoCamera()

# 	while True:
# 		frame = video_camera.get_frame()

# 		if frame != None:
# 			global_frame = frame

# 			yield (b'--frame\r\n'
#                     b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
# 		else:
# 			yield (b'--frame\r\n'
#                             b'Content-Type: image/jpeg\r\n\r\n' + global_frame + b'\r\n\r\n')

# @app.route('/video_viewer')
# def video_viewer():
#     return Response(video_stream(),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
	app.debug = True
	app.run()
