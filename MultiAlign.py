import sublime, sublime_plugin
from sublime import Settings

def get_col_tabs(view, region):
	tab_size = view.settings().get('tab_size')

	line_reg = sublime.Region(view.line(region).a, region.b)

	line_str = view.substr(line_reg)
	tab_padding_so_far = 0
	for pos, ch in [(pos, ch) for (pos, ch) in enumerate(line_str) if ch == '\t']:
		tab_padding_so_far += tab_size - ((pos+tab_padding_so_far) % tab_size) - 1

	return region.a - line_reg.a + tab_padding_so_far

class MultiAlignCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		max_col = 0
		for region in self.view.sel():
			start, end = region.a, region.b
			if start != end:
				# Don't run if some cursors have selections.
				return

			col = get_col_tabs(self.view, region)
			max_col = max(max_col, col)

		for cursor_num, (row, col) in enumerate(self.view.rowcol(x.a) for x in self.view.sel()):
			for _i in range(col, max_col):
				pass
				self.view.insert(edit, self.view.sel()[cursor_num].a, ' ')

