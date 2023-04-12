import sys
import subprocess

PACKAGES = ['setuptools==67.0.0', 'Werkzeug==2.2.2', 'Flask==2.2.2', 'Gunicorn==20.1.0', 'SQLAlchemy==2.0.0', 'iniconfig==2.0.0', 'pytest==7.2.1']

# Updates pip to the latest version
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

for package in PACKAGES:
    # Implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    package])
