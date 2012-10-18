# Sublime swap
#
# Swaps commonly used values for their logical opposites, such as:
#     top <=> bottom
#     left <=> right
#
# Also supports swapping numbers from positive to negative, allowing for
# optional unit values px, em or % at the end of the number.
#
# @author: James Warwood BSc - james.duncan.1991@googlemail.com
# @date: October 2012


import sublime, sublime_plugin, re

class js_swapCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                sublime.set_clipboard(self.view.substr(region))

                selection = self.view.substr(region)

                # Left and right swaps
                if selection == "left":
                    self.view.replace(edit, region, "right")
                    col = self.view.rowcol(self.view.sel()[0].begin())[1] + 5
                elif selection == "right":
                    self.view.replace(edit, region, "left")
                    col = self.view.rowcol(self.view.sel()[0].begin())[1] + 4

                # Top and bottom swaps
                elif selection == "top":
                    self.view.replace(edit, region, "bottom")
                    col = self.view.rowcol(self.view.sel()[0].begin())[1] + 6
                elif selection == "bottom":
                    self.view.replace(edit, region, "top")
                    col = self.view.rowcol(self.view.sel()[0].begin())[1] + 3

                # X and y swaps
                elif selection == "x":
                    self.view.replace(edit, region, "y")
                    col = self.view.rowcol(self.view.sel()[0].begin())[1] + 1
                elif selection == "y":
                    self.view.replace(edit, region, "x")
                    col = self.view.rowcol(self.view.sel()[0].begin())[1] + 1

                # Width and height swaps
                elif selection == "width":
                    self.view.replace(edit, region, "height")
                    col = self.view.rowcol(self.view.sel()[0].begin())[1] + 6
                elif selection == "height":
                    self.view.replace(edit, region, "width")
                    col = self.view.rowcol(self.view.sel()[0].begin())[1] + 5

                # Regex search for numbers like 50, -90, 30.32, -1.20px, -50%, 10em
                # Swap -ive numbers for +ive
                elif re.search('^[-+]?[0-9]\d{0,2}(\.\d{1,2})?(%)|(px)|(em)?$', selection):
                    if (selection[:1] == "-"):
                        self.view.replace(edit, region, selection[1:])
                        col = self.view.rowcol(self.view.sel()[0].begin())[1] + (len(selection)-1)
                    else:
                        # Swap + sign for - sign
                        if (selection[:1] == "+"):
                            self.view.replace(edit, region, "-"+selection[1:])
                            col = self.view.rowcol(self.view.sel()[0].begin())[1] + len(selection)
                        else:
                            self.view.replace(edit, region, "-"+selection)
                            col = self.view.rowcol(self.view.sel()[0].begin())[1] + (len(selection)+1)


                row = self.view.rowcol(self.view.sel()[0].begin())[0]
                target = self.view.text_point(row, col)

                self.view.sel().clear()
                self.view.sel().add(sublime.Region(target))

