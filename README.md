# AutoGen - WebAgent

This Python script utilizes LM Studio to create a conversational agent that describes images. The agent is designed to take a screenshot of a webpage provided by the user and then describe the contents of the screenshot in natural language.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x (3.10 in my case)
- Required Python packages (install via `pip install -r requirements.txt`):
  - `playwright`
  - `asyncio`
  - `argparse`

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies.
3. Obtain an OpenAI API key and configure it in `config.json`.
4. Run the script with the desired URL as an argument:


# Instructions

## Downloading LM Studio

You can download LM Studio from [here](https://lmstudio.ai/) or directly for your platform:

Windows: [Download](https://releases.lmstudio.ai/windows/0.2.14/latest/LM-Studio-0.2.14-Setup.exe)

Linux: [Download](https://lmstudio.ai/beta-releases.html#linux-beta)

MacOS: [Download](https://releases.lmstudio.ai/mac/arm64/0.2.14/latest/LM-Studio-0.2.14-arm64.dmg)


## Using Conda

### 1.0 Create conda environment
```
conda create -n autogen-webagent python=3.10
```

### 1.1 Activate the environment
```
conda activate autogen-webagent
```

### 1.2 Install requirements via 'requirements.txt'
```
pip install -r requirements.txt
```

### 1.3 Run the script
```
python app.py
```


# About
This is a small project of mine. Anyone who can help and has suggestions for improvement is welcome to participate.
I would also be happy about a star if you like it.

Thanks :)