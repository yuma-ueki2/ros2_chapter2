from setuptools import setup

package_name = 'my_happy'

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
    maintainer='ubuntu',
    maintainer_email='ubuntu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_happy_node = my_happy.my_happy_node:main',
               'my_happy_node2 = my_happy.my_happy_node2:main',
                  'my_happy_node3 = my_happy.my_happy_node3:main',
        ],
    },
)
