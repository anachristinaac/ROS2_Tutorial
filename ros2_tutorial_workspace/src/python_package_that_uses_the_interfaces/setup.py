from setuptools import setup

package_name = 'python_package_that_uses_the_interfaces'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='murilo',
    maintainer_email='murilomarinho@ieee.org',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'amazing_quote_publisher_node = python_package_that_uses_the_interfaces.amazing_quote_publisher_node:main',
            'subscriber_node = python_package_that_uses_the_interfaces.subscriber_node:main',
            'service_server_node = python_package_that_uses_the_interfaces.service_server_node:main',
            'service_client_node = python_package_that_uses_the_interfaces.publisher_node:main'
        ],
    },
)
