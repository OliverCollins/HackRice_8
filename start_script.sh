# Run the server
FLASK_APP=routes.py flask run

# Remove cache folder once app is finished running
rm -rf __pycache__
