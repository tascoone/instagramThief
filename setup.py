import setuptools

with open("README.md",r) as fh:
    setuptools.setup(
        name = "Instagram Thief",
        version = "1",
        scripts = ["instagramthief"],
        author = "tascoone",
        author_email = "marcotasca1106@gmail.com",
        description = 'A package for "stealing" someone else\'s instagram photos, and post them into your account.',
        long_description = long_description,
        long_description_content_type="text/markdown",
        packages = setuptools.find_packages(),
        classifier = [
            "Programming Language :: Python :: 3"
        ],       
    )
