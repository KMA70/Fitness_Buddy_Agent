# Fitness Buddy Agent

A Flask web application that embeds the **IBM watsonx Orchestrate** chat widget as an AI-powered fitness coaching assistant.

## Project Structure

```
fitness-buddy-agent/
├── app.py               # Flask application entry point
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── .env                 # Environment variables (not committed)
├── templates/
│   └── index.html       # Main page with wxO chat widget
└── static/
    └── style.css        # Application styles
```

## Prerequisites

- Python 3.9+
- An IBM watsonx Orchestrate instance with the Fitness Buddy agent deployed

## Quick Start

1. **Clone / navigate to the project folder**

   ```bash
   cd fitness-buddy-agent
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   # macOS / Linux
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment** — edit `.env` as needed:

   ```env
   FLASK_DEBUG=false
   PORT=5000
   ```

5. **Run the app**

   ```bash
   python app.py
   ```

6. Open your browser at **http://localhost:5000**

## watsonx Orchestrate Configuration

The chat widget is configured in `templates/index.html` with the following values:

| Key | Value |
|-----|-------|
| `orchestrationID` | `1a65a893a1144184bba6c6409e60a41c_d9c5c141-15dd-4e31-95f4-ad1e50f431f5` |
| `hostURL` | `https://au-syd.watson-orchestrate.cloud.ibm.com` |
| `deploymentPlatform` | `ibmcloud` |
| `agentId` | `b66563c7-35ac-43f8-bf76-41e5b8328b01` |

Update these values in `templates/index.html` if your deployment details change.

## License

MIT
