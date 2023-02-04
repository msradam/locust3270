from locust import HttpUser, task, between
from tnz.py3270 import Emulator

class TelnetUser(HttpUser):

    def on_start(self):
        self.em = Emulator(visible=True, args=["-trace",
                                  "-tracefile",
                                  "example.log"])
        self.em.connect('163.102.83.129', 992)

    def on_stop(self):
        self.em.terminate()


    def run_command(self):
        def string_wait(string):
            while True:
                self.em.wait_for_field()
                c = self.em.exec_command(b"Ascii()")
                if string in b"\n".join(c.data).decode():
                    return
        self.em.wait_for_field()
        string_wait("ENTER CHOICE")
        self.em.wait_for_field()
        self.em.send_string("TSO IBMUSER")
        self.em.send_enter()
        string_wait("ENTER PASSWORD:")
        self.em.wait_for_field()
        self.em.send_string("welcome0")
        self.em.send_enter()
        self.em.send_enter()
        self.em.send_enter()
        self.em.send_string("sdsf")
        string_wait("TEST")
        # self.em.PrintWindow()
        response = self.em.string_get()
        print(response)
        # validate response or raise an exception

    @task
    def do_async(self):
        gevent.spawn(self.run_command)

