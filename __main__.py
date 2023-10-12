import uvicorn
import argparse
import os
from server import app

def main():
    parser = argparse.ArgumentParser(description="Upload server")
    parser.add_argument('-p', '--path', type=str, default=os.getcwd(), help="Directory to store uploaded files")
    parser.add_argument('-a', '--port', type=int, default=8000, help="Port to run the server")
    args = parser.parse_args()

    # Change working directory to the path specified
    os.chdir(args.path)

    # Run server
    uvicorn.run(app, host="0.0.0.0", port=args.port)

if __name__ == "__main__":
    main()
