import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='tweetsender',
        version='1.0.0',
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
        url='https://github.com/Udomomo/tweetsender'
    )
