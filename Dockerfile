FROM python:3.13

ADD main.py .
ADD dnd_char.py .
ADD json_ops.py .
ADD key.txt .
ADD kitty_sheet.py .
ADD characters.json .

RUN pip install discord

CMD [ "python", "./main.py" ]
