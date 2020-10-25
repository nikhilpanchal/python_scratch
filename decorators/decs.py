from flask import Flask, request, abort

app = Flask(__name__)


def log_a_request(f):
    """
    Logging a request: A Decorator that doesn't take any decorator specific arguments.
    """
    def wrapped(*args, **kwargs):
        print(request.method, request.path)
        return f(*args, **kwargs)

    return wrapped

def validate_a_request(agent):
    def decorator(f):
        """
        Inner Decorator
        """
        def run_time_decorator(*args, **kwargs):
            """
            The code that will be run at run-time
            """
            if agent not in request.user_agent.string.lower():
                abort(404)
            return f(*args, **kwargs)

        return run_time_decorator

    return decorator

@app.route('/')
@log_a_request
def index():
    """
    Flask root route
    """
    return 'Hello World'

@app.route('/curl')
@validate_a_request('curl')
def curl_index():
    """
    A function to be exposed only via the curl command
    """
    return 'Hello Curl!\n'