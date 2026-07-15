from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        agent_id=os.getenv("AGENT_ID"),
        agent_env_id=os.getenv("AGENT_ENV_ID")
    )


if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    port = int(os.getenv("PORT", 5000))
    app.run(debug=debug_mode, port=port)
