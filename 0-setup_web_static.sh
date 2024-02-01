#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/

# Create a fake HTML file
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_content="server {
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }

    location /redirect_me {
        rewrite ^/redirect_me https://www.youtube.com permanent;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /usr/share/nginx/html;
        internal;
    }

    add_header X-Served-By \$hostname;
    add_header X-Frame-Options DENY;
    add_header Content-Security-Policy \"default-src 'none'\";
    add_header X-Content-Type-Options nosniff;
    add_header X-Frame-Options \"SAMEORIGIN\";

    location / {
        add_header X-Served-By \$hostname;
    }
}"
echo -e "$config_content" | sudo tee /etc/nginx/sites-available/default > /dev/null

# Restart Nginx
sudo service nginx restart

exit 0
