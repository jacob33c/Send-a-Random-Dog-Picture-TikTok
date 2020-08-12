targetBuddyPhone='‭+‭11234567890'



osascript  <<EOF
tell application "Messages"
    set theAttachment1 to POSIX file "/dogPics/dog.jpg"
    set targetService to 1st service whose service type = iMessage
    set targetBuddy to buddy "$targetBuddyPhone" of targetService
    send theAttachment1 to targetBuddy
end tell
EOF
