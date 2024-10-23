$exclude = @("venv", "bot-tkinter.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-tkinter.zip" -Force