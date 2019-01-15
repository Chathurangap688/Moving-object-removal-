import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from  mor import MovingObjectRemover

class ButtonWindow(Gtk.Window):
    remover = MovingObjectRemover()
    img=None
    def __init__(self):
        Gtk.Window.__init__(self, title="Moving Object Remover")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_mnemonic("_Open")
        button.connect("clicked", self.on_open_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Save as Jpg")
        button.connect("clicked", self.on_save_clicked)
        hbox.pack_start(button, True, True, 0)

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
            self.remover.compute_and_save(self.img,dialog.get_filename())
            #
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

win= ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()