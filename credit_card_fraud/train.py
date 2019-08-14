import mindsdb

# Instantiate a mindsdb Predictor
mdb = mindsdb.Predictor(name='cc-fraud')

# We tell the Predictor what column or key we want to learn and from what data
mdb.learn(
    from_data="dataset/creditcard-train.csv", # the path to the file where we can learn from, (note: can be url)
    to_predict='Class', # the column we want to learn to predict given all the data in the file
)