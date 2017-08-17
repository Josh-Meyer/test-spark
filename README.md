# Setup
```
# First, set up your virtual environment.
# http://docs.python-guide.org/en/latest/dev/virtualenvs/

# Now, we're going to follow this quick start guide.
# https://spark.apache.org/docs/1.6.1/quick-start.html

brew install pandoc
pip install pypandoc
pip install pyspark

brew cask install java # http://www.lonecpluspluscoder.com/2017/04/27/installing-java-8-jdk-os-x-using-homebrew/

export SPARK_LOCAL_IP="127.0.0.1"
# You should probably configure SPARK_LOCAL_IP in your ~/.bash_profile file.
# Or else you'll need to run this every time you open a new terminal.
```

## Initializing a console
```
pyspark
# The quickstart guide says to use `./bin/pyspark` to start a pyspark shell,
# but if you're using a virtual environment, it's just `pyspark`.
```

### Running Scripts
```
spark-submit --master local[4] test_spark/bin/simple_script.py
# The quickstart guide says to use `YOUR_SPARK_HOME/bin/spark-submit`,
# but if you're using a virtual environment, it's just `spark-submit`.
```
