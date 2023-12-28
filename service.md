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
sudo systemctl status file_sharing_app
```

And stop the service with:

```bash
sudo systemctl stop file_sharing_app
```

Adjust the service configuration according to your application's requirements. Ensure that the paths and permissions are set correctly, and consider adding more configuration options based on your application needs.
