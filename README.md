askGPT
A simple file summarization app using Streamlit and Google’s Gemini AI.

Features:
1.Upload any text file for summarization
2.Uses Google’s gemini-2.5-flash model to generate concise summaries
3.Interactive web interface built with Streamlit
4.Provides a smooth user experience with spinners and animations

How to Use:
1.Upload a text file using the file uploader.
2.Click the Upload button.
3.Wait a few seconds while the AI reads and summarizes the file.
4.View the summary directly on the app interface.

Requirements:
1.Python 3.x
2.streamlit
3.google-genai library
4.A Google GenAI API key

Installation & Running:
1.pip install streamlit google-genai
2.streamlit run app.py

Notes-
.Make sure to add your API key in the genai.Client(api_key="YOUR_KEY") section.
.Supports summarization for text-based files.
.For best results, upload files with clear and structured content.

Supports summarization for text-based files.

For best results, upload files with clear and structured content.
