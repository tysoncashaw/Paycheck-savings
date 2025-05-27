FROM python:latest
WORKDIR /usr/app/src

COPY main.py ./

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir streamlit
RUN pip install --no-cache-dir st_pages
RUN pip install --no-cache-dir streamlit_extras
RUN pip install --no-cache-dir validators

EXPOSE 8502

CMD [ "python", "-m",  "streamlit", "run", "./main.py", "--server.port 8502" ]