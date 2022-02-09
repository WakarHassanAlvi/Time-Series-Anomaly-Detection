# Install Libraries
```bash
pandas==1.2.4
numpy==1.20.1
matplotlib==3.3.4
sklearn
scikit-learn==0.24.1
streamlit==1.2.0
fastapi==0.70.0
uvicorn==0.15.0
aiohttp==3.8.1
python-multipart==0.0.5
seaborn==0.11.1
gunicorn==20.1.0
statsmodels==0.13.2

```
# Frontend Libraries
<h3>Streamlit</h3>
Please read the following guidelines for the <b>Streamlit</b> Setup:<br>
https://docs.streamlit.io/library/get-started/installation<br><br>

```angular2html
pip install streamlit
```

# Fast Api Backend
<h3>FastAPI</h3>
Please read the following guidelines for the <b>FastAPI</b> Setup:<br>
https://fastapi.tiangolo.com/tutorial/<br><br>

```angular2html
pip install fastapi
pip install uvicorn
pip install python-multipart
```


# RUN THIS APP LOCALLY
To run this app locally, clone the code from the <b>local branch</b> (very important). Then, set up the virtual environment in your system and run the following command:<br>
```angular2html
pip install requirements.txt
```
After that, run the following below servers:


# RUN SERVER FASTAPI
```angular2html
uvicorn api.app:app --reload
```

# RUN STREAMLIT SERVER
```angular2html
streamlit run web_app/frontend.py
```

Now your app should be running on your localhost with the port 8501. You can access it most probably with the following link:
http://localhost:8501/
