from distutils.core import setup

from importlib_metadata import entry_points

setup(name='GHuntingTool',
      version='1.0.0',
      description='This tool helps security analyst for getting artifacts of IOCs which will help to make the decision that the specfic activities are malicious or not.',
      author='Gurmukhnishan Singh',
      author_email='info@gurmukhnishansingh.me',
      packages=['GHuntingTool','GHuntingTool.Tools'],
      entry_points={
            'console_scripts': ['GHuntingTool=GHuntingTool.__main__:GHuntingTool'],
      },
      package_data={'':[
      ]}
     )