import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='marshaller',
    version='1.0.0',
    author='Miguel Caldas',
    author_email='ma.caldas331@gmail.com',
    description='}package to convert a json into an object and viceversa',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mihjovil/pymarshaller',
    project_urls={
        "Other repos": "https://github.com/mihjovil?tab=repositories"
    },
    license='MIT',
    packages=['marshaller'],
    install_requires=[],
)
