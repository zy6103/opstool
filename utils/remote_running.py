#!/opt/python3/bin/python3
# _*_ coding:utf-8 _*_
# Author: Yong
import paramiko

class RemoteHost(object):
    def __init__(self,ip,port,logname,logpwd,script_file):
        self.ip = ip
        self.port = port
        self.logname = logname
        self.logpwd = logpwd
        self.script_file = script_file
        self.conn()
    def conn(self):
        self.trans = paramiko.Transport((self.ip, self.port))
        self.trans.connect(username=self.logname, password=self.logpwd)
        self.sftp = paramiko.SFTPClient.from_transport(self.trans)
    def put_file(self):
        self.sftp.put(self.script_file,'./')
    def get_file(self):
        self.sftp.get('./','src_file')
    def run_cmd(self):
        self.ssh = paramiko.SSHClient()
        self.ssh._transport = self.trans  #将sshclient的对象的transport指定为以上的trans
        stdin,stdout,stderr = self.ssh.exec_command('sh script')
        out,err = stdout.read().decode(),stderr.read().decode()
        mess = out if out else err
        return mess
    def check(self):
        self.put_file()
        out = self.run_cmd()
        self.get_file()
        return out
    def close(self):
        self.trans.close()
