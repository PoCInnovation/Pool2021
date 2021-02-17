from nnfs_one import Model
from nnfs_one import load_dataset
from nnfs_one import Dense
from nnfs_two import Softmax_crossentropy_with_logits

X_train, y_train, X_test, y_test = load_dataset(flatten=True)

model = Model(Softmax_crossentropy_with_logits())
model.add(Dense(X_train.shape[1],100))
model.add(Dense(100, 10))
model.fit(X_train, y_train)
