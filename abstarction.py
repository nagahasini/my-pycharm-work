from abc import ABC, abstractmethod
class Notification(ABC):
    def __init__(self,msg):
        self.msg=msg
    @abstractmethod
    def send(self):
        pass

class Email(Notification):
    def __init__(self, msg):
        super().__init__(msg)
    def send(self):
        print("received {} via email".format(self.msg))


class SMS(Notification):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg=msg
    def send(self):
        print("received {} via sms".format(self.msg))

def notify_user(m):
    m.send()


e=Email('hi')
s=SMS('hi s')
notify_user(e)




