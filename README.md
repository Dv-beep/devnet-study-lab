# DevNet Study Lab

Hands-on exercises built while studying for the **Cisco DevNet Associate (DEVASC 200-901)** certification. Each folder covers a different exam domain using real Cisco platforms and APIs.

## Topics Covered

| Exam Domain | What's Here |
|---|---|
| REST APIs | HTTP GET / POST / PATCH / DELETE with `requests` |
| Cisco Platforms | Intersight compute & policy management |
| Network Programmability | NETCONF with `ncclient` and YANG models |
| Software Development | Flask API, Python OOP, `python-dotenv` |

## Project Structure

```
devnet-study-lab/
├── intersight-rest-api/       # Cisco Intersight REST API exercises
│   ├── intersight_ops.py      # CRUD operations on compute & NTP policies
│   ├── intersight_firmware.py # Firmware upgrade via API
│   ├── intersight_user_ops.py # IAM user management
│   ├── intersight_auth.py     # RSA-SHA256 request signing (Cisco auth)
│   └── .env.example           # Required environment variables
│
└── self study/                # General API & Python exercises
    ├── netconf.py             # NETCONF get-config with ncclient + YANG filter
    ├── myapi2.py              # Flask REST API (GET + POST endpoints)
    ├── alerts.py              # Poll devices, auto-create alerts for offline nodes
    ├── generates_alerts.py    # Continuous security alert simulator
    ├── create_devices.py      # Bulk device creation via POST
    ├── badge_check.py         # Badge access control logic via REST
    └── offline.py             # Filter and report offline devices
```

## Setup

### Prerequisites

- Python 3.11+
- A Cisco Intersight account with an API key (for Intersight scripts)
- A running JSON server on `localhost:3000` (for `self study/` scripts — use [json-server](https://github.com/typicode/json-server))

### Install dependencies

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r intersight-rest-api/requirements.txt
pip install flask python-dotenv ncclient xmltodict
```

### Configure credentials

The Intersight scripts load credentials from environment variables — no secrets are hardcoded.

```bash
cp intersight-rest-api/.env.example intersight-rest-api/.env
# Edit .env with your Intersight API key ID and secret key path
```

`.env` is gitignored and will never be committed.

## Resources

- [Cisco DevNet](https://developer.cisco.com) — sandboxes, learning labs, API docs
- [DevNet Associate Exam Topics](https://developer.cisco.com/certification/devnet-associate/) — official blueprint
- [Cisco Intersight API Reference](https://intersight.com/apidocs/introduction/overview/)
