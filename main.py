from gui import create_gui, create_register_gui, create_admin_approve_gui

def main():
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'register':
        create_register_gui()
    elif len(sys.argv) > 1 and sys.argv[1] == 'admin':
        create_admin_approve_gui()
    else:
        create_gui()

if __name__ == "__main__":
    main()
