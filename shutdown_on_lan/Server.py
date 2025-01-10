import argparse
from fastapi import FastAPI
import uvicorn

def Server(app: FastAPI, args: argparse.Namespace) -> None:
    """ Run the FastAPI app using Uvicorn """
    uvicorn.run(app, host="0.0.0.0", port=args.port)