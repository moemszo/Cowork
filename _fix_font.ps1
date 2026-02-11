$zipPath = "c:\Users\a\Cowork.test\知的財産権とは.pptx"
$extractPath = "c:\Users\a\Cowork.test\_pptx_temp"
if (Test-Path $extractPath) { Remove-Item $extractPath -Recurse -Force }
$tempZip = "c:\Users\a\Cowork.test\_temp.zip"
Copy-Item $zipPath $tempZip
Expand-Archive -Path $tempZip -DestinationPath $extractPath -Force
Remove-Item $tempZip
Get-ChildItem $extractPath -Recurse | Select-Object FullName
