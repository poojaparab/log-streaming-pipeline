from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    # Run the docker ps -a command and capture its output
    command_output = subprocess.run(['docker', 'ps', '-a'], capture_output=True, text=True)
    output_lines = command_output.stdout.split('\n')

    # Parse the output to get container status
    container_data = []
    for line in output_lines[1:]:
        if line.strip():  # Skip empty lines
            columns = line.split()
            container_id = columns[0]
            container_name = columns[-1]
            status ='Up' if "Up" in columns else "down"
            container_data.append({'id': container_id, 'container_name': container_name, 'status': status})

    # Render the template with container data
    return render_template('index.html', containers=container_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8111, debug=True)
