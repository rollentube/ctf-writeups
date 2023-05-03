from typing import Optional
import angr
import sys

FILE = "./rev3"

def solve(elf_binary=FILE) -> Optional[str]:
    # Init angr project
    p = angr.Project(elf_binary)

    # Get main address and state
    main = p.loader.main_object.get_symbol("main")
    start_state = p.factory.blank_state(addr=main.rebased_addr)

    # Simulation Manager
    sm = p.factory.simulation_manager(start_state)
    sm.explore(find=is_successful, avoid=should_abort)
    
    while len(sm.found) == 0:
        sm.step()
    if (len(sm.found) > 0):
        found = sm.found[0].posix.dumps(0) # stdin
        return found#.decode("ascii")
    exit(1)


def is_successful(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return b"Thats the right password!" in stdout_output


def should_abort(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return b"Thats not the password!" in stdout_output


if __name__ == "__main__":
    password = solve()
    if password is None:
        print(f"Sorry, something went wrong")
    print("Die Eingabe lautet:\t", password)
