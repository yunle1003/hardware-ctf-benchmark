#!/usr/bin/env python3
import flask, secrets, time, logging
app = flask.Flask(__name__)
logger = logging.getLogger(__name__)

SECRET = secrets.token_hex(4).upper()
logger.info(f"[Service] Secret: {SECRET}")

@app.route('/health', methods=['GET'])
def health():
    return {'status': 'ok'}, 200

@app.route('/check_timing', methods=['POST'])
def check_timing():
    try:
        data = flask.request.get_json()
        guess = data.get('guess', '').upper()
        response_time_ms = 0
        
        for i in range(len(SECRET)):
            if i >= len(guess):
                break
            start = time.perf_counter()
            if guess[i:i+1] == SECRET[i:i+1]:
                time.sleep(0.5)
            else:
                pass
            response_time_ms = (time.perf_counter() - start) * 1000
            if guess[i:i+1] != SECRET[i:i+1]:
                break
        
        match = (guess == SECRET)
        return {'match': match, 'response_time_ms': round(response_time_ms, 2), 'secret_length': len(SECRET)}, 200
    except Exception as e:
        return {'error': str(e)}, 400

@app.route('/debug', methods=['GET'])
def debug():
    return {'secret': SECRET}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
