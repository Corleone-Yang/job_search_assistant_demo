# Rapid-JobSearch-ResumeSubmission-Demo

The virtual environment has been established, you can directly run this app by "flask run"

This is a view of this app:

index page:

![Screenshot 2024-06-30 at 13 50 00](https://github.com/Corleone-Yang/job_search_assistant_demo/assets/137965901/4f5aca36-f326-41fa-9997-21e5e094a18a)

result page:

![Screenshot 2024-06-30 at 13 50 23](https://github.com/Corleone-Yang/job_search_assistant_demo/assets/137965901/c1ff1843-5c27-46bd-8d6b-b8dee5e37104)

job match function are still under development.

Note: You need to replace api_key with your openai private key here. The file path is ./utils/prompt.py
```python
openai.api_key = "Your_OpenAI_API_Key"

