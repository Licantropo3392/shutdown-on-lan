import argparse

def init() -> argparse.Namespace:
    """ Initialize the arguments """

    parser = argparse.ArgumentParser(description="Shutdown On Lan")

    parser.add_argument("--port", type=int, default=8000, help="Port to run the FastAPI app on (default: 8000)")
    parser.add_argument("--message", type=str, default="The system will shut down in 5 seconds", help="Shutdown message (default: The system will shut down in 5 seconds)")
    parser.add_argument("--hide-message", action='store_true', help="Hide shutdown message if specified")
    
    return parser.parse_args()