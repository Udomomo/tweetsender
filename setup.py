import setuptools
from os import path

if __name__ == "__main__":

    def read(fname):
        return open(path.join(path.dirname(__file__), fname)).read()

    setuptools.setup(
        name='tweetsenders',
        version='1.0.2',
        packages=setuptools.find_packages(),
        entry_points={
            'console_scripts': [
                'tweet = tweetsender.main:main'
            ],
            'tweet.command': [
                'send = tweetsender.tweet:Tweet',
                's = tweetsender.tweet:Tweet',
                'config = tweetsender.tweet:Config'
            ]
        },
        install_requires=['requests_oauthlib', 'python-dotenv', 'cliff'],
        author='Udomomo',
        author_email='batzuma@yahoo.co.jp',
        maintainer='Udomomo',
        maintainer_email='batzuma@yahoo.co.jp',
        description='Tweet-Only Twitter CLI',
        long_description=read("README.rst"),
        long_description_content_type='text/x-rst',
        url='https://github.com/Udomomo/tweetsender'
    )
