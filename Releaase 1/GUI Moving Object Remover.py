import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GdkPixbuf
from  mor import MovingObjectRemover

class ButtonWindow(Gtk.Window):
    remover = MovingObjectRemover()
    img=None
    img_computed=None
    image = Gtk.Image()
    def __init__(self):
        Gtk.Window.__init__(self, title="Moving Object Remover")
        self.set_border_width(10)
        #self.set_default_size (500,300)
        grid = Gtk.Grid()
        self.add(grid)

        button = Gtk.Button.new_with_mnemonic("_Open")
        button.connect("clicked", self.on_open_clicked)
        grid.attach(button,0, 0, 1, 1)
        
        label = Gtk.Label("                                                                             ")
        grid.attach(label,2, 0, 6, 1)

        button = Gtk.Button.new_with_mnemonic("_Save as Jpg")
        button.connect("clicked", self.on_save_clicked)
        grid.attach(button,8, 0, 1, 1)

        
        #button.connect("clicked", self.on_save_clicked)
        self.image.set_from_file('./tmp.jpg')
        grid.attach(self.image,0, 2, 9, 1)
        label = Gtk.Label("                                                                             ")
        grid.attach(label,2, 1, 6, 1)

        self.set_resizable(False)
    def on_click_me_clicked(self, button):
        print("\"Click me\" button was clicked")

    def on_open_clicked(self, button):
        dialog = Gtk.FileChooserDialog("Please Select a folder", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(100, 100)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Folder selected: " + dialog.get_filename())
            ##
            self.img=self.remover.open_image_set(dialog.get_filename())
            self.img_computed=self.remover.compute_and_save(self.img,'./tmp.jpg')
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                filename="./tmp.jpg", 
                width=24, 
                height=24, 
                preserve_aspect_ratio=True)

            self.image = Gtk.Image.new_from_pixbuf(pixbuf)
            #self.image.set_from_file('./tmp.jpg')
            dialog.set_default_size(100, 100)

            #
            ##
        elif response == Gtk.ResponseType.CANCEL:
            print("Canceled")

        dialog.destroy()
        

    def on_save_clicked(self, button):
        dialog = Gtk.FileChooserDialog("Save As JPG", self,
            Gtk.FileChooserAction.SAVE,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_SAVE, Gtk.ResponseType.OK))

        #self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            #
            self.remover.save_image(self.img_computed,dialog.get_filename())
            #
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

win= ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()