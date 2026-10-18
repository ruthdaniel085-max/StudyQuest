import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)

# Initialize the Gemini client
client = genai.Client()


@app.route("/")
def home():
  return jsonify({"message": "StudyQuest Backend is Running!"})


@app.route("/api/parse-syllabus", methods=["POST"])
def parse_syllabus():
  if "file" not in request.files:
    return jsonify({"error": "No syllabus file uploaded"}), 400

  file = request.files["file"]
  file_path = file.filename
  file.save(file_path)

  # Upload to Gemini File API
  uploaded_file = client.files.upload(file=file_path)

  prompt = (
      "Analyze this course syllabus. Extract all exams, quizzes, homework,"
      " and reading tasks with due dates. Return them strictly as a valid JSON"
      " array of objects with keys: title, type, due_date, and suggested_points."
  )

  response = client.models.generate_content(
      model="gemini-3.8-flash", contents=[uploaded_file, prompt]
  )

  return jsonify({"schedule": response.text})


if __name__ == "__main__":
  app.run(debug=True, port=5000)