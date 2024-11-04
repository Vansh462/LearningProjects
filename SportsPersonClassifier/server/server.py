from flask import Flask,request,jsonify
from flask_cors import CORS
import util

app=Flask(__name__)
CORS(app)

@app.route('/classify_image',methods=['GET','POST'])
def classify_image():
    try:
        image_data = request.form.get('image_data')

        if not image_data:
            return jsonify({"error": "No image data provided 1"}), 400

        if not image_data.startswith('data:image/'):
            return jsonify({"error": "Invalid image data format 1"}), 400

        # Process the image data
        result = util.classify_image(image_data)
        return jsonify(result)

    except Exception as e:
        app.logger.error(f"Error processing image: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__=="__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(host="0.0.0.0",port=5001)