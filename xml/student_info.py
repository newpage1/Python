#coding=utf-8

class sc:
	def __init__(self,sname,sid,sgrade,cid,cname,teacher,cscore,idx):
		self.__sname = sname
		self.__sid = sid
		self.__sgrade = sgrade
		self.__cid = cid
		self.__cname = cname
		self.__teacher = teacher
		self.__cscore = cscore

	        self.__idx = idx

	def print_info(self):
		print " NO.%s record in XML"%self.__idx
		print " <sname> : %s "%self.__sname
		print " <sid> : %s "%self.__sid
		print " <sgrade> : %s "%self.__sgrade
		print " <course> "
		print " <cid> : %s "%self.__cid
		print " <cname> : %s  "%self.__cname
		print " <teacher> : %s  "%self.__teacher
		print " <score> : %s"%self.__cscore
