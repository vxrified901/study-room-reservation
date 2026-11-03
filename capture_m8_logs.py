
import logging
import app

with open("m8_sample_logs.jsonl", "w", encoding="utf-8") as log_file:
    handler = logging.StreamHandler(log_file)
    handler.setFormatter(logging.Formatter("%(message)s"))

    app.logger.addHandler(handler)

    try:
        client = app.app.test_client()
        response = client.get("/")
        assert response.status_code == 200
    finally:
        app.logger.removeHandler(handler)
        handler.close()

print("Structured logs saved to m8_sample_logs.jsonl")
