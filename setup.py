from distutils.core import setup

setup(
    name='django-rest-messages',
    version=__import__('django_rest_messages').__version__,
    description='User-to-user messaging API for Django',
    long_description=open('README.rst').read(),
    author='Michael Petychakis',
    author_email='hello@apilama.com',
    url='https://github.com/mpetyx/django-rest-messages',
    install_requires=[
        'Django',
        'djangorestframework'
    ],
    packages=(
        'django_rest_messages',
        'django_rest_messages.templatetags',
        'django_rest_messages.migrations',
    ),
    package_data={
        'django_rest_messages': [
            'templates/django_rest_messages/*',
            'templates/notification/*/*',
            'locale/*/LC_MESSAGES/*',
        ]
    },
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Framework :: Django',
    ),
)
