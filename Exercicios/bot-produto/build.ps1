$exclude = @("venv", "bot-produto.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-produto.zip" -Force