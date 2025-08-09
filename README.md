# Multi-Roles Chat Application

A Streamlit-based chat application that allows users to interact with different AI agents (roles) with distinct personalities and behaviors.

## Features

- **Multiple AI Roles**: Choose between different AI characters (currently "小樱" and "易大师")
- **Conversation Memory**: Maintains chat history for each role separately
- **Streamlit UI**: Clean and interactive web interface
- **Cached Agents**: Efficient resource management with cached agent instances

## File Structure

- **main.py**: Main application logic and UI

- **agent.py**: Agent class implementation

- **config.py**: Configuration settings

- **prompt.py**: Prompt templates and system messages

- **README.md**: This documentation file

## Usage

### Installation

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run main.py
```