#!/usr/bin/env python

"""
Simple Script that fires up Python SimpleHTTPServer to host powershell scripts. 
It also prints a comma separated list you can easily drop into MSF's Powershell Interactive Payloads. 

@awhitehatter
"""

import os, sys, argparse, re, SimpleHTTPServer, SocketServer

#parse arguments
def argsparser(psdir, ipaddr, port):
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p', type=str, required=True, help='Path for .ps1 files')
    parser.add_argument('--host', '-i', type=str, required=True, help='<ip>:<port>')

    args = parser.parse_args()

    psdir = args.path
    ipport = args.host

    ipaddr = str(ipport).split(':')[0]
    port = str(ipport).split(':')[1]
    
    return (psdir, ipaddr, port)

#main_function
def main():

    psdir = ''
    ipaddr = ''
    port = ''

    psdir, ipaddr, port = argsparser(psdir, ipaddr, port)

    #verify path exists
    if os.path.isdir(psdir):
        print('[*] Directory found\n')
        os.chdir(psdir)
    else:
        print('[X] Directory not found, please check and try again')
        sys.exit(0)

    #Store .ps1 files for printing
    pslist = []
    pstxt = ''
    
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(".ps1"):
                pslist.append(os.path.join(root,file))

    for i in pslist:
        pstxt += ' http://'+ ipaddr + ':' + port + i + ','
    
    pstxt = re.sub('\.\/','/', pstxt)

    print '\n[*] Copy and paste the below to MSF:\n'
    print pstxt.rstrip(',')
    print '\n[*] Now starting webserver\n'

    port = int(port)
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", port), Handler)

    try:
        print "[*] serving at port", port
        httpd.serve_forever()
    except:
        print '\n[x] quitting...'
        exit()


if __name__ == '__main__':
    main()
