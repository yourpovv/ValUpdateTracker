<div align="center">


# ValorantUpdateTracker


**Posts a Discord notification when VALORANT updates**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Language](https://img.shields.io/badge/Python-logoColor=white)

<img width="873" height="613" alt="image" src="https://github.com/user-attachments/assets/9189a183-bb48-4fcf-b0dc-6a1463e7364a" />


</div>

## Usage

Download from: [Releases](../../releases)


* Create a Discord webhook and copy it
* Run `ValorantUpdateTracker.exe`, paste the webhook when asked
* Keep it running

Checks **https://valorant-api.com/v1/version** every 15 minutes

### Running it on GitHub instead

* Fork this repo
* Go to **Settings > Secrets and variables > Actions**, **Repository secrets** tab (not Environment secrets), **New repository secret**: name it `DISCORD_WEBHOOK_URL`, paste your webhook
* Go to the **Actions** tab and click **I understand my workflows, go ahead and enable them**
* [check-version.yml](.github/workflows/check-version.yml)

## Build

needs Python 3.10+

```bash
git clone https://github.com/<your-fork>/ValorantUpdateTracker.git
cd ValorantUpdateTracker
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

set `DISCORD_WEBHOOK_URL=` in `.env`, then:

```bash
py -m src.launcher
```

### Compiling the exe

```bash
pip install -r requirements-build.txt
pyinstaller --onefile --name ValorantUpdateTracker src/launcher.py
```

Outputs `dist/ValorantUpdateTracker.exe`. Pushing a tag like `v1.0.0` builds and publishes this automatically via [release.yml](.github/workflows/release.yml)

## License

MIT. See [LICENSE](LICENSE)
