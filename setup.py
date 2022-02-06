from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fcm_notification/__init__.py
from fcm_notification import __version__ as version

setup(
	name="fcm_notification",
	version=version,
	description="Sends Frappe notifications to devices via Firebase Cloud Message",
	author="Raheeb",
	author_email="rahibhassan.10@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
