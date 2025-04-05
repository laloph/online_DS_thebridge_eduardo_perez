# limpiar_git.ps1 - Script para eliminar archivos grandes y limpiar GitHub

Write-Host "Eliminando rastreo de Git LFS..."
git lfs untrack "*.csv"
git lfs untrack "*.npz"

if (Test-Path ".gitattributes") {
    Remove-Item .gitattributes -Force
}

git add .gitattributes
git commit -m "Eliminando rastreo LFS de archivos grandes"

Write-Host "Eliminando archivos pesados del historial..."

git filter-branch --force --index-filter `
"git rm --cached --ignore-unmatch Project_Break_II_ML/data/covtype.csv && git rm --cached --ignore-unmatch Sprint_17/Unidad_01/Practica_Obligatoria/data/data.npz" `
--prune-empty --tag-name-filter cat -- --all

Write-Host "Actualizando archivo .gitignore..."
Add-Content .gitignore "Project_Break_II_ML/data/covtype.csv"
Add-Content .gitignore "Sprint_17/Unidad_01/Practica_Obligatoria/data/data.npz"

git add .gitignore
git commit -m "Ignorando archivos grandes para evitar errores en GitHub"

Write-Host "Haciendo push forzado al repositorio remoto..."
git push origin --force

Write-Host "✅ Repositorio limpiado y actualizado sin archivos pesados."
