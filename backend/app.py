import os
from pathlib import Path

from quart import Quart, send_from_directory


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FRONTEND_DIR = PROJECT_ROOT / "frontend"

app = Quart(__name__)


@app.get("/")
async def index():
    return await send_from_directory(FRONTEND_DIR, "index.html")


@app.get("/<path:filename>")
async def frontend_file(filename: str):
    return await send_from_directory(FRONTEND_DIR, filename)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="127.0.0.1", port=port, debug=True)
