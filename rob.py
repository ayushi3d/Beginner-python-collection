
import subprocess

if __name__  == '__main__':
    print("Welcome to Robospeaker Python Project created by ayushi")
    while True:
        x = input("What you want me to speak: ")
        if x == "q":
            break
        command = f'echo {x} | PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak([Console]::In.ReadToEnd())"'
        subprocess.run(command, shell=True)

