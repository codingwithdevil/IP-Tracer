#
#    IP-Tracer   by Coding With Devil  https://www.youtube.com/c/CodingWithDevil/
#    This tool is used for Trace Ip address Location 
#    Also this tool is only for Education Purpose only
#    This program comes with ABSOLUTELY NO WARRANTY
#    The use of the Ip-Tracer & its resources is COMPLETE RESPONSIBILITY of the END-USER.
#    Developers assume NO liability and are NOT responsible for any damage caused by this program.

import Defs.runner.runner as main_runner

if __name__ == '__main__':
    try:
        main_runner.main()
    except KeyboardInterrupt: 
        print("""
        \033[1;31m Keyboard interrupted
        """)
        exit(3)
