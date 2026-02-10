#/bin/bash 
set -e 
 
echo "Running database migrations..." 
python scripts/setup_db.py 
 
echo "Starting application..." 
exec uvicorn src.app:app --host 0.0.0.0 --port 8000 
