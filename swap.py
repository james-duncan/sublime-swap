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

# Loads swaps from the "enabled_categories" list of the supplied settings object.
#
# @param settings    The settings to load swaps from (e.g.: default or user)
# @param swaps       The current list of swaps (or an empty array if this is the first call to this method)
#
# @return    The original swaps array argument, with the addition of any new swaps from the supplied settings object
def load_swaps(categories, settings):

    swaps = []

    if categories != None:

        for s in settings:
            for c in categories:
                categorySwaps = s.get(c)

                if categorySwaps != None:
                    for curSwap in categorySwaps:

                        if swaps:

                            count = 0
                            exists = False

                            # Check if any of the target words exist in the array of swaps already
                            while count < len(swaps):
                                if len(set(curSwap) & set(swaps[count])):
                                    exists = True

                                count += 1

                            # Add the array if it has cleared validation
                            if not exists:
                                swaps = swaps + [curSwap]

                        # First item
                        else:
                            swaps = swaps + categorySwaps

    return swaps

def load_settings():
    # User settings
    userSettings = sublime.load_settings('swap-user.sublime-settings')
    userCategories = userSettings.get('enabled_categories')

    # Default settings
    defaultSettings = sublime.load_settings('swap-default.sublime-settings')

    # Categories
    categories = defaultSettings.get('enabled_categories')

    if userCategories != None:
        categories = list(set(categories) | set(userCategories))

    print categories

    swaps = load_swaps(categories, [userSettings, defaultSettings])

    return swaps

class swapCommand(sublime_plugin.TextCommand):
    # Cache
    swap_cache = []

    def run(self, edit):

        if not self.swap_cache:
            swaps = load_settings()
            self.swap_cache = swaps
            print "Fetched swaps from disk"
        else:
            swaps = self.swap_cache
            print "Used cached swaps"

        for region in self.view.sel():
            if not region.empty():
                sublime.set_clipboard(self.view.substr(region))

                selection = self.view.substr(region)

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


