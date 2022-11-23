import virtualbox
vbox = virtualbox.VirtualBox()
session = virtualbox.Session()

newVM = virtualbox.VirtualBox()

def showVirtualMachines():
    print([m.name for m in vbox.machines])

def standUpVM(nameVM):
    machine = vbox.find_machine(nameVM)
    #if Virtual is 6.1 and below use the next
    #progress = machine.launch_vm_process(session, "gui", "")
    #else
    # For virtualbox API 6_1 and above (VirtualBox 6.1.2+), use the following:
    progress = machine.launch_vm_process(session, "gui", [])
    progress.wait_for_completion()

def consultingVM():
    print(session.state)
    #If the answer is => SessionState(2)  # locked

def writeVM(sentence):
    session.console.keyboard.put_keys(sentence)

def loginVM(user, password):
    guest_session = session.console.guest.create_session(user, password)

def powerDownVM():
    session.console.power_down()

def createVM(nameVM):
    vm = newVM.create_machine("",nameVM,[],"ubuntu64Guest","")
    newVM.register_machine(vm)

def deleteVM(nameVM):
    machineBorrar = newVM.find_machine(nameVM)
    machineBorrar.remove()


     
 
showVirtualMachines()
createVM('Ubuntu')
