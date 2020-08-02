from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="django-web-monetization",
    version="0.2",
    packages=["monetization", "monetization.migrations"],
    url="https://github.com/LloydTao/django-web-monetization",
    license="MIT",
    author="Lewis Lloyd",
    author_email="Lewis_Lloyd@live.co.uk",
    description="A simple integration for the Web Monetization API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
