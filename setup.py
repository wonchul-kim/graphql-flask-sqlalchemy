from setuptools import setup, find_packages 

with open('README.md', encoding='utf-8') as f: # README.md 내용 읽어오기
        long_description = f.read()

setup(
        name                    = 'myDB',
        version                 = '0.0.1', 
        long_description        = long_description, 
        long_description_content_type = 'text/markdown', 
        description             = 'Algorithms to create database at AIV Corp.',
        author                  = 'AIV',
        author_email            = 'kim.wonchul@aiv.ai',
        url                     = 'http://192.168.10.41:8079/aivdb', 
        # download_url        = 'https://github.com/TooTouch/tootorch/archive/v0.1.tar.gz', 
        # install_requires    =  ["torch","torchvision","h5py","tqdm","pillow","opencv-python"], # requirements will do this
        packages                = find_packages(exclude = []),
        keywords                = ['AIV','DB'], 
        python_requires         = '>=3.8',
        package_data            = {"": ['*.yaml', "*.txt", "*.md"]},
        include_package_data    = True,
        zip_safe                = False,
        classifiers             = [   
            'GraphQL :: Graphene :: SqlAlchemy :: PostgreSQL',
            'Flask',
        ],
    )