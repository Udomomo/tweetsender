import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='tweetsender',
        version='0.0.1',
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
        url='http://udomomo.hatenablog.com/'
    )
