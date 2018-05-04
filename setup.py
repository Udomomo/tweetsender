import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='tweet',
        version='0.0.1',
        packages=setuptools.find_packages(),
        entry_points={
            'console_scripts': [
                'tweet = tweet.main:main'
            ]
        },
        install_requires=['requests_oauthlib', 'python-dotenv'],
        author='Udomomo',
        author_email='batzuma@yahoo.co.jp',
        url='http://udomomo.hatenablog.com/'
    )
