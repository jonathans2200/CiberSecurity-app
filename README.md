# CiberSecurity App

A web application designed for cybersecurity analysis, allowing authenticated users to scan files, URLs, and IP addresses for potential threats using the VirusTotal API, WhoisXMLAPI and an LLM from OpenAI. It features a Vue.js frontend, multiple FastAPI backends, and utilizes Docker Compose for orchestration.

## Features

*   **File Analysis:** Upload files to scan for malware and known threats via VirusTotal.
*   **URL Analysis:** Submit URLs to check against VirusTotal's database of malicious sites.
*   **IP Address Analysis:** Check the reputation and history of IP addresses with VirusTotal.
*   **Advanced URL Analysis:** In-depth URL scanning capabilities (including phishing, malware checks, SSL verification, and Whois verification).
*   **User Authentication:** Secure user login and management provided by Auth0.
*   **API Gateway:** Centralized API routing and management via Kong.

*(Note: Frontend analysis features currently use simulated responses and require full backend integration.)*

## Technology Stack

*   **Frontend:** Vue.js 3, Vuetify, TypeScript, Auth0 Client SDK
*   **Backend (VirusTotal Service):** Python 3, FastAPI, Uvicorn, `aiohttp` (for VT API), OpenAI.
*   **Backend (MCP Service):** Python 3, FastAPI, Uvicorn, MCP (Model Context Protocol from Anthropic) to use external/internal tools and data to enrich responses, and OpenAI.
*   **Database:** PostgreSQL (Separate instances for VT service and MCP service)
*   **API Gateway:** Kong
*   **Containerization:** Docker, Docker Compose
*   **Database Management:** Adminer

## Project Structure
```
├── Backend/ # FastAPI application for VirusTotal integration (Service: api)
│ ├── config/ # Configuration files (e.g., vt_client.py)
│ ├── .env # CREATE 1ST .env file
│ ├── Dockerfile
│ └── requirements.txt
├── Frontend/ # Vue.js frontend application
│ ├── public/
│ ├── src/
│ ├── auth_config.json # Auth0 configuration (Client-side)
│ ├── Dockerfile # (Optional: If building/serving frontend via Docker)
│ └── package.json
├── mcp-client/ # Additional FastAPI service (Service: fastapi)
│ ├── .env CREATE 2nd .env file
│ └── Dockerfile
├── kong/ # Kong API Gateway configuration
│ └── kong.yml
├── pg_db/ # Init scripts for the mcp-client database (db_mcp)
│ └── init.sql
├── .gitignore # Git ignore rules
├── .env (CREATE EN EMPTY .env file here)
├── docker-compose.yml # Docker Compose configuration for all services
└── README.md
```

## Prerequisites

*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/) (Usually included with Docker Desktop)
*   VirusTotal API Key ([Get one here](https://developers.virustotal.com/reference/getting-started))
*   Auth0 Account and Application configured ([Auth0](https://auth0.com/))
*   OpenAI API Key
*   WhoisXMLAPI API Key

## Setup and Running

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/jonathans2200/CiberSecurity-app.git
    cd CiberSecurity-app
    ```

2.  **Configure Environment Variables:**

    *   **Crear un archivo .env**

        **For ./Backend:**
        *  OpenAI API Key:
        OPENAI_KEY=your-openai-api-key-here
        * VirusTotal API Key: 
        VT_KEY=your-virustotal-api-key-here
        * Database connection URL:
        DATABASE_URL=postgresql://postgres:postgres@db:5432/virustotaldb
        * Auth0 Client ID: 
        AUTH0_CLIENT_ID=your-auth0-client-id-here
        * Auth0 Domain:
        AUTH0_DOMAIN=your-auth0-domain-here

        **For ./mcp-client:**
        *  OpenAI API Key:
        OPENAI_API_KEY=your-openai-api-key-here
        * VirusTotal API Key: 
        VT_API_KEY=your-virustotal-api-key-here
        * Database connection URL:
        DATABASE_URL=postgresql://pguser:pgpass@db_mcp:5432/cybersec
        * MCP Server CMD: 
        MCP_SERVER_CMD=python mcp_server.py
        * WhoisXMLAPI API Key:
        WHOIS_API_KEY=your-WhoisXMLAPI-here

        **For the root, .env is necessary, leave it blank.**

    *   **Backend (VirusTotal Service):**
        *   Create `Backend/.env`
        *   Populate `Backend/.env`

    *   **Backend (MCP Service):**
        *   Create `mcp-client/.env`
        *   Populate `mcp-client/.env`

    *   **Frontend (Auth0):**
        *   Configure `Frontend/auth_config.json` with your Auth0 Domain, Client ID, and Audience. The audience should match the identifier for your backend APIs secured by Auth0 (e.g., `https://securescan.com/api/v3/`).

3.  **Build and Start Containers:**
    Run the following command from the project root directory:
    ```bash
    docker-compose up --build -d
    ```
    *   `--build`: Forces Docker to rebuild the images if the Dockerfiles or their contexts have changed.
    *   `-d`: Runs the containers in detached mode (in the background).

4.  **Accessing Services:**
    Once the containers are up, the services should be accessible at:
    *   **Kong Gateway (Proxy):** `http://localhost:8002` (Your primary access point for backend APIs)
    *   **Kong Admin API:** `http://localhost:8003`
    *   **VirusTotal Backend API (Direct):** `http://localhost:8000` (Service name: `api`)
    *   **MCP Backend API (Direct):** `http://localhost:8001` (Service name: `fastapi`)
    *   **Adminer (Database GUI):** `http://localhost:8081`
    *   **Frontend:** Access depends on how it's served. If running locally during development (e.g., `npm run serve` from `Frontend/`), it's often `http://localhost:5173` (Vite default) or `http://localhost:8080`. If served via Docker/Kong, it would likely be accessed through the Kong Gateway port (`8002`). *(This needs clarification based on deployment strategy)*

## Configuration

*   **Environment Variables:** Critical configuration (API keys, database URLs) is managed via `.env` files in the respective service directories (`Backend/`, `mcp-client/`). **Do not commit `.env` files to Git.**
*   **API Routing:** Kong handles routing requests from the gateway (`:8002`) to the backend services. Configuration is defined in `kong/kong.yml`.
*   **Authentication:** Auth0 configuration is split:
    *   `Frontend/auth_config.json` for the Vue client.
    *   Backend services will need to be configured to validate JWTs issued by your Auth0 tenant, using the specified Audience.

## API Endpoints

The main backend API endpoints are exposed via the **Kong Gateway** (`http://localhost:8002`). Refer to the `kong/kong.yml` configuration and the FastAPI application code (`Backend/main.py`, `mcp-client/main.py` for specific routes. Some include:

*   `/logs` (GET)
*   `/analyze` (POST)
*   `/profile` (GET)
*   `/advanced-analysis` (POST)

*(Authentication using JWT Bearer tokens obtained via Auth0 is not yet implemented)*

## Stopping the Application

To stop all running containers defined in the `docker-compose.yml`:

```bash
docker-compose down
```

To stop and remove volumes (clears database data):

```bash
docker-compose down -v
```

## License

**MIT**
