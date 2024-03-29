from setuptools import setup

setup(
    name="studio-api",
    version="0.0.1",
    description="""Django app for handling REST-API in Studio""",
    url="https://www.scaleoutsystems.com",
    include_package_data=True,
    package=["api"],
    package_dir={"api": "."},
    python_requires=">=3.6,<4",
    install_requires=[
        "django==4.2.1",
        "requests==2.31.0",
        "django-guardian==2.4.0",
        "django-tagulous==1.3.3",
        "django-filter==22.1",
        "drf-nested-routers==0.93.4",
        "minio==7.0.2",
        "s3fs==2022.1.0",
    ],
    license="Copyright Scaleout Systems AB. See license for details",
    zip_safe=False,
    keywords="",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
