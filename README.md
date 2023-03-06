# Instructions

## Download

Download the package from GitHub

```shell
git clone https://github.com/coderaidershaun/chatbot-conversation-jarvis.git chatbot
```

## Setup backend

Change directory into backend

```shell
cd chatbot/backend
```

### Setup virtual environment

Create a Virtual Environment

```shell
python3 -m venv venv
```

Activate Virtual Environment (MAC)

```shell
source venv/bin/activate
```

Activate Virtual Environment (Windows)

```shell
source venv/Scripts/activate
```

Upgrade PIP

```shell
pip3 install --upgrade pip
```

### Install Python packages

Install required Python packages

```shell
pip3 install openai python-decouple fastapi "uvicorn[standard]" python-multipart
```

Or use this alternative method (although this alternative method might not work if using Windows)

```shell
pip3 install -r requirements.txt
```

### Create Environment Variables

Create your .env file

```shell
touch .env
```

Update your .env file with the following. You can see your .env by typing sudo nano .env or just by clicking on the file if you are in VS Code.

```plain
OPEN_AI_ORG=enter-you-key-here
OPEN_AI_KEY=enter-you-key-here
ELEVEN_LABS_API_KEY=enter-you-key-here
```

### Start your backend server

Start your backend server

```shell
uvicorn main:app
```

Alternatively, you can ensure your server resets every time you make a change by typing:

```shell
uvicorn main:app -- reload
```

You can check your server is working by going to:

```plain
http://localhost:8000/health
```

## Setup frontend

Change directory into frontend

```shell
cd ..
cd chatbot/frontend
```

Install packages

```shell
yarn --exact
```

Build application

```shell
yarn build
```

Start server in dev mode

```shell
yarn dev
```

You can check your dev server is working by going to:

```plain
http://localhost:5173/health
```

or alternatively in live mode:

```shell
yarn start
```

You can check your live server is working by going to:

```plain
http://localhost:4173/health
```
