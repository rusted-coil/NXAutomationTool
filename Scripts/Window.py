class Window:
    def __init__(self, master=None):
        # Window設定
        master.title('NX Automation Tool')
        master.geometry('1280x720')

        # PainterViewを作成
#        view = PainterView(master)

        # PainterControllerを作成
#        controller = PainterController(view)
        
if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    app = Window(root)
    root.mainloop()
