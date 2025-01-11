import argparse
from fastapi import FastAPI
import uvicorn

loggingConfig = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "server.log",
            "formatter": "default",
        },
    },
    "loggers": {
        "uvicorn": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

def Server(app: FastAPI, args: argparse.Namespace) -> None:
    """ Run the FastAPI app using Uvicorn """
    uvicorn.run(app, host="0.0.0.0", port=args.port, log_config=loggingConfig)