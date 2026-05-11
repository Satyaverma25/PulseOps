import time
import threading
import psutil
from flask import Flask, jsonify, Response, render_template_string, request
from prometheus_client import Counter, Gauge, Histogram, generate_latest

app = Flask(__name__)

# ✅ Metrics
REQUEST_COUNT = Counter("sensor_requests_total", "Total sensor requests", ["endpoint"])
CPU_USAGE = Gauge("cpu_usage_percent", "CPU usage percent")
MEMORY_USAGE = Gauge("memory_usage_percent", "Memory usage percent")

REQUEST_LATENCY = Histogram(
    "request_latency_seconds",
    "Request latency in seconds",
    ["endpoint"]
)

# Global values
latest_latency = 0.0
cpu = 0
memory = 0

# ✅ Background system monitoring
def background_work():
    global latest_latency, cpu, memory
    while True:
        start = time.time()

        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent

        CPU_USAGE.set(cpu)
        MEMORY_USAGE.set(memory)

        latest_latency = time.time() - start
        time.sleep(1)

# ✅ Decorator for latency tracking
def track_latency(endpoint_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            latency = time.time() - start
            REQUEST_LATENCY.labels(endpoint=endpoint_name).observe(latency)
            return result
        return wrapper
    return decorator

# ✅ Dashboard UI
@app.route("/")
def dashboard():
    return render_template_string(f"""
    <html>
    <head>
        <title>Sensor Dashboard</title>
        <meta http-equiv="refresh" content="2">
        <style>
            body {{
                font-family: Arial;
                background: linear-gradient(to right, #1e3c72, #2a5298);
                color: white;
                text-align: center;
            }}
            .container {{
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 40px;
            }}
            .card {{
                background: rgba(255,255,255,0.1);
                padding: 30px;
                margin: 20px;
                border-radius: 15px;
                width: 250px;
            }}
        </style>
    </head>
    <body>

        <h1>🚀 Sensor Monitoring Dashboard</h1>

        <div class="container">
            <div class="card">
                <h2>💻 CPU Usage</h2>
                <h1>{cpu}%</h1>
            </div>

            <div class="card">
                <h2>🧠 Memory Usage</h2>
                <h1>{memory}%</h1>
            </div>

            <div class="card">
                <h2>⏱️ Latency</h2>
                <h1>{round(latest_latency, 4)} sec</h1>
            </div>

            <div class="card">
                <h2>📡 Status</h2>
                <h1>{"⚠️ High Load" if cpu > 70 else "✅ Normal"}</h1>
            </div>
        </div>

    </body>
    </html>
    """)

# ✅ Sensor API
@app.route("/sensor")
@track_latency("sensor")
def sensor():
    REQUEST_COUNT.labels(endpoint="sensor").inc()
    return jsonify({
        "cpu": cpu,
        "memory": memory
    })

# ✅ Metrics endpoint
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

# ✅ Run app
if __name__ == "__main__":
    threading.Thread(target=background_work, daemon=True).start()
    app.run(host="0.0.0.0", port=8000)