# coding=utf-8
from optparse import *
from optparse import OptionGroup
from ntru import *
import ast

if __name__ == '__main__':
    parser = OptionParser("""
        
                _                _   _ _____ _____   _____ 
           | |              | \ | |_   _|  __ \ / ____|
      _ __ | |_ _ __ _   _  |  \| | | | | |  | | (___  
     | '_ \| __| '__| | | | | . ` | | | | |  | |\___ \ 
     | | | | |_| |  | |_| | | |\  |_| |_| |__| |____) |
     |_| |_|\__|_|   \__,_| |_| \_|_____|_____/|_____/ 
                                                   
                                                   
    -option ['1','2','3'] 
        1:pour generer une clé public
        2:pour generer un message crypte
        3: decypter le message
                
    -n parametre 1
    -p parametre 2
    -q parametre 3
    -P [public key]
    
    -M message (list)
    -r message crypte
    
    example 1: generation d'une clé public:
    python2.7 ntrunids.py -o 1 -n 11 -p 20 -q 300 
    
    exemple 2: (cryptage de message) avec clé public: 
    python2.7 ntrunids.py -n 11 -p 20 -q 300 -o 2 -P "[108, 116, 101, 71, 255, 124, 115, 279, 20, 128, 183]" -M "[1, 0, 1, 0, 1, 1, 1]"
    
    exemple 3: decryptage
    python2.7 ntrunids.py -n 11 -p 20 -q 300 -o 3 -r "[141, 240, 281, 140, 221, 61, 241, 0, 0, 120, 60]"

    
    """)
    parser.add_option("-M" ,"--set_message",dest="umessage",type="string",help="")

    parser.add_option("-P" ,"--set_public_key",type="string",dest="upublickey",help="")

    parser.add_option("-o" ,"--option",dest="uoption",type="string",help="")

    parser.add_option("-r" ,"--rr",dest="umc",type="string",help="")

    parser.add_option("-n","--n",dest="un",type="int",help="random v")
    parser.add_option("-p","--p",dest="up",type="int",help="random v")
    parser.add_option("-q","--q",dest="uq",type="int",help="random v")


    (options, args) = parser.parse_args()

    if options.uoption ==None:

        print(parser.usage)
        exit(0)
    elif options.uoption=="1" and options.un != None and options.up != None and options.uq != None :
        n=int(options.un)
        p=int(options.up)
        q=int(options.uq)
        #print ("hh ",n,p,q)

        V1 = Ntru(n, p, q)
        f = [1, 1, -1, 0, -1, 1]
        g = [-1, 0, 1, 1, 0, 0, -1]
        d = 2
        V1.genPublicKey(f, g, 2)
        pub_key = V1.getPublicKey()
        print "*****",type(pub_key)
        print "les parametres: n={} p={} q={} la cle publique {}".format(n,p,q,pub_key)

    elif options.uoption=="2" and options.uoption=="1" and options.un != None and options.up != None and options.uq != None and options.upublickey!=None and options.umessage !=None:


        n = int(options.un)
        p = int(options.up)
        q = int(options.uq)
        msg =options.umessage
        public_key=options.upublickey
        msg = options.umessage
        msg=ast.literal_eval(msg)

        print msg
        print public_key

        V2 = Ntru(n, p, q)
        pub_key = options.upublickey
        public_key=ast.literal_eval(public_key)


        V2.setPublicKey(public_key)
        ranPol = [-1, -1, 1, 1]
        encrypt_msg = V2.encrypt(msg, ranPol)
        print "Encrypted Message          : ", encrypt_msg
    elif options.uoption=="3" and options.umc!=None:
        n = int(options.un)
        p = int(options.up)
        q = int(options.uq)
        # print ("hh ",n,p,q)
        message_crypte=options.umc
        message_crypte=ast.literal_eval(message_crypte)
        print type(message_crypte)

        V1 = Ntru(n, p, q)
        f = [1, 1, -1, 0, -1, 1]
        g = [-1, 0, 1, 1, 0, 0, -1]
        d = 2
        V1.genPublicKey(f, g, 2)

        print "plain text message :",V1.decrypt(message_crypte)
    else:
        print(parser.usage)
        exit(0)