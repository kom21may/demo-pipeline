from setuptools import setup,find_packages

setup(name="census-income",version="0.0.1",
      author="komal",
      author_email="komalkumari199905@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )

#find package will search those folder who have __init__.py file