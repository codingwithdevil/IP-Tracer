#
#    IP-Tracer   by Coding With Devil  https://www.youtube.com/c/CodingWithDevil/
#    This program comes with ABSOLUTELY NO WARRANTY
#    The use of the YTE & its resources is COMPLETE RESPONSIBILITY of the END-USER.
#    Developers assume NO liability and are NOT responsible for any damage caused by this program.

import requests as rqs
import json
import Defs.theme.theme as theme 
import subprocess as sp
import Defs.pallette.palette as plt
from time import sleep as wait
default_palette = plt.default_palette

def main():
    sp.run("clear")
    print(theme.mainlogo)
    print("""\033[1;34mWhat is the ip 
    """)
    ip = input("{0}    Iplocator {1}>>> {2}".format(default_palette[1],default_palette[2],default_palette[3]))
    try :
        url = f"http://ip-api.com/json/{ip}"
        res = rqs.get(url)
        data = json.loads(res.content)
        if data['status'] == 'success':
            sp.run("clear")
            print(theme.minilogo)
            wait(2)
            print(f"""

\033[1;32m Ip Information of \033[1;31m{data['query']}

\033[1;33m[\033[1;32m+\033[1;33m] \033[1;34m Status       \033[1;31m: \033[1;32m{data['status']}

\033[1;33m[\033[1;32m+\033[1;33m] \033[1;34m Country      \033[1;31m: \033[1;32m{data['country']}

\033[1;33m[\033[1;32m+\033[1;33m] \033[1;34m CountryCode  \033[1;31m: \033[1;32m{data['countryCode']}

\033[1;33m[\033[1;32m+\033[1;33m] \033[1;34m Region       \033[1;31m: \033[1;32m{data['region']}

\033[1;33m[\033[1;32m+\033[1;33m] \033[1;34m Region Name  \033[1;31m: \033[1;32m{data['regionName']}

\033[1;33m[\033[1;32m+\033[1;33m] \033[1;34m City         \033[1;31m: \033[1;32m{data['city']}

\033[1;33m[\033[1;32m+\033[1;33m] \033[1;34m ZipCode      \033[1;31m: \033[1;32m{data['zip']}

\033[1;33m[\033[1;32m+\033[1;33m] \033[1;34m lat          \033[1;31m: \033[1;32m{data['lat']}

\033[1;33m[\033[1;32m+\033[1;33m] \033[1;34m lon          \033[1;31m: \033[1;32m{data['lon']}

\033[1;33m[\033[1;32m+\033[1;33m] \033[1;34m TimeZone     \033[1;31m: \033[1;32m{data['timezone']}

\033[1;33m[\033[1;32m+\033[1;33m] \033[1;34m ISP          \033[1;31m: \033[1;32m{data['isp']}

\033[1;33m[\033[1;32m+\033[1;33m] \033[1;34m ORG          \033[1;31m: \033[1;32m{data['org']}

\033[1;33m[\033[1;32m+\033[1;33m] \033[1;34m As           \033[1;31m: \033[1;32m{data['as']}

        """)
            wait(5)
            print("""\033[1;33m  
Notes:- 
    You will probably not know the exact physical address of an Internet device (mobile phone, computer, etc.), website, or the person you're trying to locate,
    but in most cases you will know the region (district), and very often accompanying details such as area, or metro, along with latitude and longtitude
    which is quite enough information when you are doing your own investigation and you also want to see
    those details on the visual map as well.
    \033[1;31mI Will Try To Make It To a Accurate Out\n
    """)
            print("\033[1;32m Information Collecting Finished")
            wait(10)
            exit()

        else :
            print("\033[1;31m Unknown Error Occured \n ")
            exit(3)
    except rqs.HTTPError:
        print("\033[1;31m Cant reach to the server\n")
        exit(3)       
    except Exception as e:
        print("\033[1;31m Unknown Error Occured\n")