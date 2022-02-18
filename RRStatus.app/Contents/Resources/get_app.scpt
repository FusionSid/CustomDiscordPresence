tell application "System Events"
  tell (first process whose frontmost is true)
    set appName to displayed name
    set appPath to ((path to frontmost application) as text)
  end tell
end tell

tell application appPath
  set appID to id
end tell

return (appName & appPath)