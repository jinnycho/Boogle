# Boogle

Boogle is an LLM-powered answering machine designed to answer any question from multiple sources as simply as possible.

![Alt Text](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcm5iY3M4aGNkbGd3dXgwbGNmcGtpZGFzNGE2ZGF2NTIxb2Ewb2YzMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WoLhFt0i6AtUFasPyC/giphy.gif)

## To Run
1. Create and activate a Python virtual environment if needed:

   ```sh
   source .venv/bin/activate
   uv pip install -r requirements.txt
   ```

2. `npm run build`: compiles `frontend/src/main.ts` into `frontend/dist/main.js`.
   This command is expected to finish immediately after compiling.

3. `npm run watch`: keeps TypeScript running and recompiles whenever you save a
   file in `frontend/src`.

4. `npm start`: compiles the TypeScript, then uses `uv` to start a Quart server
   at `http://127.0.0.1:5000`.
