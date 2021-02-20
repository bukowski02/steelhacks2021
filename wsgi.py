from app.main import app 
import db

if __name__ == "__main__": 
        db.dbInit()
        app.run()