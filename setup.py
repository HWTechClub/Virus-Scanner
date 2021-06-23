import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='vscan',
     version='0.1',
     author="HWU Sec Team",
     author_email="pranavc10@hotmail.com",
     description="A cli tool that uses APIs to scan malicious files & urls",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/HWTechClub/Virus-Scanner",
     packages=["virus_scanner","virus_scanner/Main","virus_scanner/Meta_Defender","virus_scanner/VirusTotal_API"],
     scripts=["vscan"],
     install_requires=['pyyaml',
            'tkintertable',
            'pyfiglet',
            'pypi-cli',
            'PyInquirer'
                       ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
         "Operating System :: OS Independent",
     ],
 )
