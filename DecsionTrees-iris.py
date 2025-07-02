from site import makepath
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz




iris= load_iris()# This loads the iris data
X= iris[:,2:]#Select all rows and columns from index 2 onwards
y=iris.target#Its a 1D array containing the labels(0,1 or 2) for each flower
tree_clf=DecisionTreeClassifier(max_depth=2)#Atleast 2 levels of decision.Not counting the final leaf nodes
tree_clf.fit(X,y)#This train the decision trees using X and y
#This model learns how to split the data data based on petal length and width to classify flowers correctly
#Training builds the tree structure, which can then use to make or predictions or visualize
#Visualize the decision tree
#Create a file describing the decision tree in a format that can be visualized
#Create .dot file is a text in the Graphiz format which can be a converted into image(PNG or PDF)
export_graphviz(
    tree_clf,#Creating trainded decision tree model
    out_file=image_path("iris_tree.dot"),#Where the tree description is saved.image_path is function
    feature_names=iris.feature_names[2:],#Names of the features used in (['petal length (cm)', 'petal width (cm)'])
    class_names=iris.target_names,
    rounded=True,
    filled=True,
)


#.dot file is a text file in the Graphiz format which can be converted into a image
$ dot -Tpng iris_tree.dot -o iris_tree.png
#This creates a visual image of the decision tree that you can open and view.


tree_clf.predict([[5,1.5]])
tree_clf.predict([[5,1.5]])

#Performing regression tasks
tree_reg= DecisionTreeClassifier(max_depth=2)
tree_reg(X,y)














































