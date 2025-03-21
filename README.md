# **Docker Workshop - Prerequisites**

## 1. System Requirements
To ensure a smooth hands-on experience, participants should have the following:

- **Operating System:** Windows 10/11 (Pro, Enterprise, or Education), macOS (Intel or M1/M2).
- **Processor:** 64-bit processor with virtualization enabled in BIOS.
- **RAM:** Minimum 4GB (8GB recommended).
- **Disk Space:** At least 10GB free for Docker images and containers.

---

## 2. Installing Docker

### **For Windows (Using winget)**
1. Open PowerShell and run:
   ```sh
   winget install -e --id Docker.DockerDesktop
   ```
2. Restart your system after installation.
3. Open **Docker Desktop**. The first time it runs, it will open a terminal window asking to install **WSL 2** (Windows Subsystem for Linux). Follow the on-screen instructions to complete the installation.
4. After WSL is installed, restart your system again.
5. Open **Docker Desktop** and ensure it is running.
6. Verify the installation by running:
   ```sh
   docker --version
   ```

### **For macOS**
1. Download **Docker Desktop for Mac** from: [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
2. Open the downloaded `.dmg` file and drag Docker to **Applications**.
3. Launch Docker and grant necessary permissions if prompted.
4. Verify the installation using Terminal:
   ```sh
   docker --version
   ```

---

## 3. Installing Docker Compose (If Not Installed by Default)
Run the following command to check:
```sh
docker-compose --version
```
If not installed, follow these steps:
- **Windows/macOS**: Included with Docker Desktop.

---

## 4. Additional Tools (Optional but Recommended)
- **VS Code** (for writing Dockerfiles & managing containers): [Download VS Code](https://code.visualstudio.com/)
- **Postman** (for testing APIs inside containers): [Download Postman](https://www.postman.com/downloads/)

---

## 5. Basics of Node.js and React.js
Participants are expected to have a basic understanding of:
- **Node.js**: Installation, running scripts, package management with npm/yarn.
- **React.js**: Component-based structure, state management, and basic project setup.

If you are new to these technologies, consider reviewing their official documentation:
- [Node.js](https://nodejs.org/)
- [React.js](https://react.dev/)

---

## 6. Verifying Docker Installation
After installation, confirm Docker is running correctly:
1. Run:
   ```sh
   docker run hello-world
   ```
2. If you see a welcome message, Docker is installed successfully.

---

## 7. Setup Before the Workshop
- Install Docker and verify installation.
- Ensure VS Code is installed.
- Review Node.js and React.js basics if needed.
- Join the workshop on time with Docker running!

🚀 **See you at the workshop!**

