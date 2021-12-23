# Mac-only commands
if [[ $OSTYPE == 'darwin'* ]]; then
    alias ls='ls -hG'
    alias ports="netstat -ap tcp | grep -i \"listen\""
    alias ports2="sudo lsof -i -P | grep LISTEN"
    alias trash="rmtrash"
    
    alias checkrain="/Applications/checkra1n.app/Contents/MacOS/checkra1n"
    alias obs="open -n -a OBS.app"
    alias idea="open -a Intellij\ IDEA.app"
    alias xcode="open -a Xcode.app"

    # Java
    export JDK8="/usr/local/opt/openjdk@8/libexec/openjdk.jdk/Contents/Home"
    export JDK11="/usr/local/opt/openjdk@11/libexec/openjdk.jdk/Contents/Home"
    export JDK16="/usr/local/opt/openjdk@16/libexec/openjdk.jdk/Contents/Home"
    export JDK17="/usr/local/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home"
    alias java8="${JDK8}/bin/java"
    alias java11="${JDK11}/bin/java"
    alias java16="${JDK16}/bin/java"
    alias java17="${JDK17}/bin/java"
    export JAVA_HOME=${JDK11}
    export PATH="${JDK11}/bin:$PATH"
fi
