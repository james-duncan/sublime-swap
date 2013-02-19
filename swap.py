# Sublime swap
#
# Swaps commonly used values for their logical opposites, such as:
#     top <=> bottom
#     left <=> right
#
# Also supports swapping numbers from positive to negative, allowing for
# optional unit values px, em or % at the end of the number.
#
# @author: James Warwood - james.duncan.1991@googlemail.com
# @date: October 2012
import sublime, sublime_plugin, re



class swapCommand(sublime_plugin.TextCommand):

    # Cache
    swap_cache = {}

    # ...
    #
    # @param settings   An array of settings objects, in order of precedence
    #
    # @return
    def load_swaps(self, allSettings, ext):

        print ext

        # Array of swaps
        swaps = []


        for settings in allSettings:
            setting = settings.get(ext)

            if setting != None:

                # Each indivdual array of swaps
                for swapArray in setting:

                    if swaps:
                        count = 0
                        exists = False

                        # Check if any of the target words exist in the array of swaps already
                        while count < len(swaps):

                            # Set dupe flag if already exists
                            if len(set(swapArray) & set(swaps[count])):
                                exists = True

                            # Increment counter
                            count += 1


                        # Add the array if it has cleared validation
                        if not exists:
                            swaps = swaps + [swapArray]


                    # First item
                    else:
                        swaps = swaps + [swapArray]

        return swaps

    def load_settings(self):
        # User settings
        userSettings = sublime.load_settings('swap-user.sublime-settings')

        # Default settings
        defaultSettings = sublime.load_settings('swap-default.sublime-settings')

        return {
            "user_settings": userSettings,
            "default_settings": defaultSettings
        }

    def run(self, edit):

        # File extension
        file_name = self.view.file_name()
        ext = file_name[file_name.rfind('.')+1:]

        if not self.swap_cache.get(ext):

            # Load user and default settings
            settings = self.load_settings()

            swaps = self.load_swaps([settings['user_settings'], settings['default_settings']], ext)

            if swaps:
                self.swap_cache[ext] = swaps
        else:
            swaps = self.swap_cache[ext]

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

                        # # Clear and add
                        # @TODO fix this
                        # if settings.get('deselect') == True:
                        #     self.view.sel().clear()

                        self.view.sel().add(sublime.Region(target))