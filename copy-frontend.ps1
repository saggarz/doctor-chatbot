# Copy frontend build files to root for Vercel deployment
Copy-Item -Path "frontend/dist/index.html" -Destination "." -Force
Copy-Item -Path "frontend/dist/assets" -Destination "." -Recurse -Force
Write-Host "Frontend files copied to root directory"
