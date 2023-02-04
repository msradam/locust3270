from py3270 import Emulator

em = Emulator(visible=True, args=["-trace",
                                  "-tracefile",
                                  "example.log"])

def string_wait(string):
    while True:
        em.wait_for_field()
        c = em.exec_command(b"Ascii()")
        if string in b"\n".join(c.data).decode():
            return

em.connect('163.102.83.129', 992)
em.wait_for_field()
string_wait("ENTER CHOICE")
em.wait_for_field()
em.send_string("TSO IBMUSER")
em.send_enter()
string_wait("ENTER PASSWORD:")
em.wait_for_field()
em.send_string("welcome0")
em.send_enter()
em.send_enter()
em.send_enter()
em.send_string("sdsf")
em.send_enter()
response = em.string_get()
print(response)
string_wait("TEST")
# em.PrintWindow()


def string_wait(string):
    while True:
        em.wait_for_field()
        c = em.exec_command(b"Ascii()")
        if string in b"\n".join(c.data).decode():
            return

#         em.exec_command(b"Wait(Output)")


# string_wait("Enter:  ")
# em.send_string("xrfmcl userid\\n")

# string_wait("Password  ===> ")
# em.send_string("password\\n")

# # if your host unlocks the keyboard before truly being ready you can use:
# em.wait_for_field()

# # maybe look for a status message
# string_wait("ICH70001I")

# # do something useful
# string_wait("***")
# em.send_enter()
# string_wait("READY")
# em.send_string("logon\\n")
# string_wait("LOGGED OFF")

# disconnect from host
# em.terminate()