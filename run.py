from app import app

if __name__ == '__main__':
    # Run the Flask application in debug mode
    # In production, debug should be set to False
    app.run(host='0.0.0.0', port=5000, debug=True)