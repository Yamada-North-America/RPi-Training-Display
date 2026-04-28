# Script-Recovery.ps1
# Monitors and relaunches the Training Display script if it stops running

param(
    [int]$CheckInterval = 30,  # Check every 30 seconds
    [string]$ScriptPath = "/mnt/Training/RPi-Training-Display/Training-Display.py",
    [string]$LaunchCommand = "python3 $ScriptPath >/dev/null 2>&1 &"
)

function IsProcessRunning {   
    try {
        # Check if python3 process is running the Training-Display script
        $process = Get-Process python3 -ErrorAction SilentlyContinue | 
                   Where-Object { $_.CommandLine -like "*Training-Display*" }
        return $null -ne $process
    }
    catch {
        return $false
    }
}

function StartTrainingDisplay {
    param([string]$Command)
    
    try {
        Invoke-Expression $Command
        Write-Host "$(Get-Date): Training Display script launched" -ForegroundColor Green
        return $true
    }
    catch {
        Write-Host "$(Get-Date): Failed to launch Training Display script: $_" -ForegroundColor Red
        return $false
    }
}

# Main monitoring loop
Write-Host "$(Get-Date): Starting Training Display Monitor" -ForegroundColor Cyan

while ($true) {
    if (-not (IsProcessRunning)) {
        Write-Host "$(Get-Date): Training Display script not running. Relaunching..." -ForegroundColor Yellow
        StartTrainingDisplay $LaunchCommand
    }
    
    Start-Sleep -Seconds $CheckInterval
}