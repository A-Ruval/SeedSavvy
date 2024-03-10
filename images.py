from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Define the Contentful API endpoint and access token
API_ENDPOINT = "https://cdn.contentful.com/spaces/hfvx97g6kjey/environments/master/assets"
ACCESS_TOKEN = "KWIwUOAB6aQkzbtVXctJ77djcoFdpROY0q6cWCL2RCY"

# Route to handle requests for fetching seed images
@app.route("/get_seed_image", methods=["POST"])
def get_seed_image():
    seed_type = request.form.get("seedType").lower()
    image_url = fetch_image_url(seed_type)

    if image_url:
        return jsonify({"imageUrl": image_url})
    else:
        return jsonify({"error": "Image not found for the entered seed type."}), 404

# Function to fetch image URL from Contentful API based on seed type
def fetch_image_url(seed_type):
    url = f"{API_ENDPOINT}?access_token=KWIwUOAB6aQkzbtVXctJ77djcoFdpROY0q6cWCL2RCY&query={seed_type}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get("items") and data["items"]:
            # Get the first image matching the seed type
            return data["items"][0]["fields"]["file"]["url"]
        else:
            return None
    else:
        return None