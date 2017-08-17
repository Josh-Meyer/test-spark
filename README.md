Testing PySpark

# https://spark.apache.org/docs/1.6.1/quick-start.html

brew install pandoc
pip install pypandoc
pip install pyspark

brew cask install java # http://www.lonecpluspluscoder.com/2017/04/27/installing-java-8-jdk-os-x-using-homebrew/

export SPARK_LOCAL_IP="127.0.0.1"

# quickstart guide says to use `./bin/pyspark` to start a spark shell,
# but because I use a virtual environment, it's actually just `pyspark` for me.
pyspark
