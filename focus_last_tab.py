import sublime_plugin

class LastViewCommand(sublime_plugin.WindowCommand):
    def run(self):
        group = self.window.active_group()
        self.window.focus_view(self.window.views_in_group(group)[-1])
