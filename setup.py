from setuptools import setup, find_packages

setup(
    name="asyncFontCompiler",
    version="0.0.1",
    description="A python package to compile fonts asnychoronously inside RF.",
    author="Bahman Eslami",
    author_email="contact@bahman.design",
    url="http://bahman.design",
    license="Apache 2.0",
    platforms=["Any"],
    package_dir={"": "asyncFontCompiler.roboFontExt/lib"},
    packages=find_packages("asyncFontCompiler.roboFontExt/lib"),
    install_requires=[],
    python_requires=">=3.7",
)
