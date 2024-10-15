$exclude = @("venv", "bot-formulario.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-formulario.zip" -Force