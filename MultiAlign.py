import sublime_plugin

class MultiAlignCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        max_col = -1
        for row, col in (self.view.rowcol(x.a) for x in self.view.sel()):
            max_col = max(max_col, col)

        for cursor_num, (row, col) in enumerate(self.view.rowcol(x.a) for x in self.view.sel()):
            for _i in range(col, max_col):
                self.view.insert(edit, self.view.sel()[cursor_num].a, ' ')
