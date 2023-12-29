To run EchoSync app as a service on Linux, you can create a systemd service. systemd is a system and service manager for Linux, and it provides a straightforward way to manage services. Here's an example of how you can create a systemd service for your Python file sharing app.

1. Create a new service file. Open a terminal and run:

   ```bash
   sudo nano /etc/systemd/system/file_sharing_app.service
   ```

   Replace `file_sharing_app` with an appropriate name for your service.

2. Add the following content to the file:

   ```ini
   [Unit]
   Description=File Sharing App
   After=network.target

   [Service]
   ExecStart=/path/to/your/run.sh
   WorkingDirectory=/path/to/your/app
   User=your_username
   Group=your_group
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

   Make sure to replace `/path/to/your/run.sh`, `/path/to/your/app`, `your_username`, and `your_group` with the actual paths and user/group information.

3. Save the file and exit the editor.

4. Reload systemd to pick up the changes:

   ```bash
   sudo systemctl daemon-reload
   ```

5. Start and enable the service:

   ```bash
   sudo systemctl start file_sharing_app
   sudo systemctl enable file_sharing_app
   ```

Now, your file sharing app should be running as a service. You can check the status with:

```bash
sudo systemctl status echosync
```

And stop the service with:

```bash
sudo systemctl stop echosync
```
If you want to use a custom host name like "echosync," you can do so, but keep in mind that this will only work if "echosync" is resolvable to an IP address on your local machine. Typically, for local development, you would use either "localhost" or "127.0.0.1" as the host, as these are common aliases for the loopback address.

If you want to use a custom host name, you need to ensure that your machine can resolve it. One way to do this is by adding an entry to your system's hosts file. Here's an example for Unix-based systems (Linux, macOS):

```bash
sudo nano /etc/hosts
```

Add the following line at the end of the file:

```plaintext
127.0.0.1   echosync.com
```

Save the file and exit.

Then, in your Flask application:

```python
from flask import Flask

app = Flask(__name__)

# Your Flask routes and configuration go here

if __name__ == '__main__':
    # Use the custom host name
    app.run(debug=False, host='127.0.0.1', port=80)
```

Now, when you run your Flask app, it should be accessible at `http://echosync.com/` in your web browser.

Keep in mind that using "localhost" or "127.0.0.1" is usually more straightforward for local development, and using custom host names might introduce complications depending on your system configuration.

Adjust the service configuration according to your application's requirements. Ensure that the paths and permissions are set correctly, and consider adding more configuration options based on your application needs.
