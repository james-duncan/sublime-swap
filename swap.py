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

settings = sublime.load_settings('swap.sublime-settings')

class swapCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                sublime.set_clipboard(self.view.substr(region))

                selection = self.view.substr(region)

                # List of swaps
                swapCategories = settings.get('swaps')

                swaps = []
                for sc in swapCategories:
                    swaps = swaps + settings.get(sc)

                # Loop through array of swap arrays
                for s in swaps:

                    # If selection is in the current subarray
                    if selection in (s):

                        # Get index of selection and replacement
                        index = s.index(selection)
                        replacement = s[(index+1) % len(s)]

                        # Replace text
                        self.view.replace(edit, region, replacement)

                        # Set focus row and col
                        row = self.view.rowcol(self.view.sel()[0].begin())[0]
                        col = self.view.rowcol(self.view.sel()[0].begin())[1] + (len(replacement))
                        target = self.view.text_point(row, col)

                        # Clear and add
                        if settings.get('deselect') == True:
                            self.view.sel().clear()

                        self.view.sel().add(sublime.Region(target))
                        return;


                # Regex search for numbers like 50, -90, 30.32, -1.20px, -50%, 10em
                # Swap -ive numbers for +ive
                # if re.search('^[-+]?[0-9]\d{0,2}(\.\d{1,2})?(%)|(px)|(em)?$', selection):
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


