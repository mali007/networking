__author__ = 'ali007'

import ftplib

class FtpClient (object):

    def __init__(self,ftpserver,user = "", password = ""):
        self.ftpserver = ftpserver
        self.user = user
        self.passowrd = password

    def contact_ftp(self):
        f = ftplib.FTP(self.ftpserver)
        try:
            f.login(self.user,self.passowrd)
            if f.getwelcome().__contains__("220"):
                print "connected "
                print f.cwd("/pub/dvd")

                print f.dir()

        except:
            print "error occurred "

user = ""
password = ""
server = "alpha.greenie.net"
obj = FtpClient(server,user,password)
obj.contact_ftp()


