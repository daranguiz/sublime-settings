import sublime, sublime_plugin

class WpuatRunCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        import subprocess
        subprocess.Popen([r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", r"C:\darioa_lab\source\qcom\qct\platform\winmobile\EA\workspaces\wufan\automation\main\wpuat.ps1"])