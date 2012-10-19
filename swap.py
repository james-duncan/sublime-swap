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

class swapCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                sublime.set_clipboard(self.view.substr(region))

                selection = self.view.substr(region)

                # List of swaps
                swaps = []
                swaps.append(["left", "right"])
                swaps.append(["top", "bottom"])


                # Loop through array of swap arrays
                for s in swaps:

                    # If selection is in the current subarray
                    if selection in (s):

                        # Get index of selection and replacement
                        index = s.index(selection)
                        replacement = s[0] if index == 1 else s[1]

                        # Replace text
                        self.view.replace(edit, region, replacement)

                        # Set focus row and col
                        row = self.view.rowcol(self.view.sel()[0].begin())[0]
                        col = self.view.rowcol(self.view.sel()[0].begin())[1] + (len(replacement))
                        target = self.view.text_point(row, col)

                        # Clear and add
                        self.view.sel().clear()
                        self.view.sel().add(sublime.Region(target))


                # # X and y swaps
                # elif selection == "x":
                #     self.view.replace(edit, region, "y")
                #     col = self.view.rowcol(self.view.sel()[0].begin())[1] + 1
                # elif selection == "y":
                #     self.view.replace(edit, region, "x")
                #     col = self.view.rowcol(self.view.sel()[0].begin())[1] + 1

                # # Width and height swaps
                # elif selection == "width":
                #     self.view.replace(edit, region, "height")
                #     col = self.view.rowcol(self.view.sel()[0].begin())[1] + 6
                # elif selection == "height":
                #     self.view.replace(edit, region, "width")
                #     col = self.view.rowcol(self.view.sel()[0].begin())[1] + 5

                # # Get/set
                # elif selection == "get":
                #     self.view.replace(edit, region, "set")
                #     col = self.view.rowcol(self.view.sel()[0].begin())[1] + 3
                # elif selection == "set":
                #     self.view.replace(edit, region, "get")
                #     col = self.view.rowcol(self.view.sel()[0].begin())[1] + 3

                # # show/hide
                # elif selection == "show":
                #     self.view.replace(edit, region, "hide")
                #     col = self.view.rowcol(self.view.sel()[0].begin())[1] + 4
                # elif selection == "hide":
                #     self.view.replace(edit, region, "show")
                #     col = self.view.rowcol(self.view.sel()[0].begin())[1] + 4

                # # min/max
                # elif selection == "min":
                #     self.view.replace(edit, region, "max")
                #     col = self.view.rowcol(self.view.sel()[0].begin())[1] + 3
                # elif selection == "max":
                #     self.view.replace(edit, region, "min")
                #     col = self.view.rowcol(self.view.sel()[0].begin())[1] + 3

                # # true/false
                # elif selection == "true":
                #     self.view.replace(edit, region, "false")
                #     col = self.view.rowcol(self.view.sel()[0].begin())[1] + 5
                # elif selection == "false":
                #     self.view.replace(edit, region, "true")
                #     col = self.view.rowcol(self.view.sel()[0].begin())[1] + 4

                # # inner/outer
                # elif selection == "inner":
                #     self.view.replace(edit, region, "outer")
                #     col = self.view.rowcol(self.view.sel()[0].begin())[1] + 5
                # elif selection == "outer":
                #     self.view.replace(edit, region, "inner")
                #     col = self.view.rowcol(self.view.sel()[0].begin())[1] + 5

                # # Regex search for numbers like 50, -90, 30.32, -1.20px, -50%, 10em
                # # Swap -ive numbers for +ive
                # elif re.search('^[-+]?[0-9]\d{0,2}(\.\d{1,2})?(%)|(px)|(em)?$', selection):
                #     if (selection[:1] == "-"):
                #         self.view.replace(edit, region, selection[1:])
                #         col = self.view.rowcol(self.view.sel()[0].begin())[1] + (len(selection)-1)
                #     else:
                #         # Swap + sign for - sign
                #         if (selection[:1] == "+"):
                #             self.view.replace(edit, region, "-"+selection[1:])
                #             col = self.view.rowcol(self.view.sel()[0].begin())[1] + len(selection)
                #         else:
                #             self.view.replace(edit, region, "-"+selection)
                #             col = self.view.rowcol(self.view.sel()[0].begin())[1] + (len(selection)+1)

