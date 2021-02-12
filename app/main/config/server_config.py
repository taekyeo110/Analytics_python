import os
from dotenv import load_dotenv
load_dotenv()

config = {
    "production": {
        "DEBUG": False,

    },
    "development": {
        "DEBUG": True,
    },
    "test": {
        "DEBUG": True,
        "TESTING": True,
        "PRESERVE_CONTEXT_ON_EXCEPTION": False,
    }
}

SERVER_ENV = os.getenv('SERVER_ENV')
SERVER_PORT = os.getenv('SERVER_PORT')
