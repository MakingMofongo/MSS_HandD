        app.quit()  # Quit the current application
        python = sys.executable
        os.execl(python, python, *sys.argv)