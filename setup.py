import os

from setuptools import find_packages, setup


setup(
    name='django-roman',
    version='0.1',
    description='A Django template filter to convert Arabic numerals to Roman numerals',
    long_description=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.rst')).read(),
    author='Richard Cornish',
    author_email='rich@richardcornish.com',
    url='https://github.com/richardcornish/django-roman',
    license='BSD',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=('tests',)),
    test_suite='smarty.tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
