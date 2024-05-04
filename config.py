import os
import dotenv

dotenv.load_dotenv()

MONGODB_URI: str = os.environ['MONGODB_URI']
DATABASE_NAME: str = os.environ['DATABASE_NAME']
