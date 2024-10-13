import configparser as cp, sys; c=cp.ConfigParser(); c.read(sys.argv[1]); c.setdefault(sys.argv[2],{})[sys.argv[3]]=sys.argv[4]; c.write(open(sys.argv[1],'w'))
