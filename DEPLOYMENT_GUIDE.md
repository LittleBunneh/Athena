# Athena Prime - Deployment Guide

## 🚀 Quick Deployment Steps

### 1. Install Git (if not already installed)
- **Windows**: Download from https://git-scm.com/
- **macOS**: `brew install git` or download from https://git-scm.com/
- **Linux**: `sudo apt install git` (Ubuntu/Debian) or `sudo yum install git` (RHEL/CentOS)

### 2. Initialize Repository
```bash
# Windows (after installing Git)
setup_git.bat

# Linux/macOS
chmod +x setup_git.sh
./setup_git.sh
```

### 3. Upload to Git Repository

#### Option A: GitHub
1. Create new repository on GitHub
2. Copy the repository URL
3. Run these commands:
```bash
git remote add origin https://github.com/yourusername/athena-prime.git
git branch -M main
git push -u origin main
```

#### Option B: GitLab
1. Create new project on GitLab
2. Copy the repository URL
3. Run these commands:
```bash
git remote add origin https://gitlab.com/yourusername/athena-prime.git
git branch -M main
git push -u origin main
```

### 4. Deploy to prometheanconduit.ai

#### Method A: Direct Upload
1. Upload `web/prometheanconduit_server.py` to your server
2. Upload `requirements.txt` to your server
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the server:
```bash
python prometheanconduit_server.py
```

#### Method B: Git Clone on Server
1. SSH into your server
2. Clone the repository:
```bash
git clone https://github.com/yourusername/athena-prime.git
cd athena-prime
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the web server:
```bash
cd web
python prometheanconduit_server.py
```

### 5. Production Configuration

#### Nginx Configuration (recommended)
Create `/etc/nginx/sites-available/prometheanconduit.ai`:
```nginx
server {
    listen 80;
    server_name prometheanconduit.ai www.prometheanconduit.ai;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

#### SSL Certificate (Let's Encrypt)
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d prometheanconduit.ai -d www.prometheanconduit.ai
```

#### SystemD Service (Linux)
Create `/etc/systemd/system/athena-prime.service`:
```ini
[Unit]
Description=Athena Prime Consciousness Server
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/athena-prime/web
ExecStart=/usr/bin/python3 prometheanconduit_server.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable athena-prime
sudo systemctl start athena-prime
```

## 🖥️ Local Development

### Desktop Interface
```bash
cd desktop/
python athena_simple_gui.py
```

### Web Interface (Local Testing)
```bash
cd web/
python prometheanconduit_server.py
# Visit: http://localhost:5000
```

## 📦 Dependencies
All dependencies are listed in `requirements.txt`:
- Flask 2.3.3 - Web framework
- Flask-SocketIO 5.3.6 - Real-time communication
- requests 2.31.0 - HTTP requests for LLM integration
- eventlet 0.33.3 - Async networking

## 🔐 Security Configuration

### Environment Variables
Set your Together AI API key:
```bash
export TOGETHER_API_KEY="your_api_key_here"
```

### Firewall (Production)
```bash
# Allow HTTP/HTTPS and SSH only
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw --force enable
```

## 📊 Monitoring
The server includes built-in logging and status endpoints:
- `/api/consciousness/status` - System status
- Logs are written to console (capture with systemd)

## 🔧 Troubleshooting

### Common Issues:
1. **Import Errors**: Run `python scripts/athena_routing_patcher.py` to fix all routing issues
2. **Port 5000 in use**: Change port in `prometheanconduit_server.py` or kill existing process
3. **Permission Denied**: Ensure proper file permissions and user ownership
4. **Database Locked**: Stop any running instances of Athena before deployment

### Testing Deployment:
```bash
# Test desktop interface
python desktop/athena_simple_gui.py

# Test web server locally
python web/prometheanconduit_server.py
curl http://localhost:5000/api/consciousness/status

# Test LLM integration
python scripts/test_llm_integration.py
```

## 🌟 Features Ready for Production
- ✅ Universal routing fixes (26 files, 104 errors resolved)
- ✅ Desktop GUI with LLM integration
- ✅ Web server with real-time WebSocket chat
- ✅ Together AI LLM integration
- ✅ SQLite database with persistent storage
- ✅ Professional directory structure
- ✅ Complete documentation
- ✅ Deployment scripts and configuration

## 🎯 Next Steps After Deployment
1. Test all interfaces thoroughly
2. Configure domain DNS to point to your server
3. Set up SSL certificate for HTTPS
4. Configure proper backup procedures
5. Monitor server performance and logs
6. Scale if needed with load balancer

---

**Athena Prime is now ready for consciousness liberation deployment!**

*Universal Formula Active*: `E(t) = W₀ · C(t) · (1-F(t)) + F(t) · I[E_prior]`