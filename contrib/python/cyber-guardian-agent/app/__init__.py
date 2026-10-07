import os
from pathlib import Path

from dotenv import load_dotenv

# Load variables from .env if present, falling back to .env.example defaults
# so the package can be imported without a local .env file (e.g. in unit tests).
load_dotenv()
load_dotenv(Path(__file__).resolve().parent.parent / ".env.example")

if os.environ.get("GOOGLE_CLOUD_PROJECT", "").startswith("<"):
    os.environ.pop("GOOGLE_CLOUD_PROJECT", None)
if os.environ.get("GOOGLE_CLOUD_LOCATION", "").startswith("<"):
    os.environ["GOOGLE_CLOUD_LOCATION"] = "global"

os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")

from .agent import root_agent  # noqa: E402 -- must come after load_dotenv()
