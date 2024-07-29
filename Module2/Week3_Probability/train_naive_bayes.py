import numpy as np

def create_train_data():
    
    data = [['Sunny','Hot','High', 'Weak', 'no'],
            ['Sunny', 'Hot', 'High', 'Strong', 'no'],
            ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
            ['Rain', 'Mild', 'High', 'Weak' ,'yes'],
            ['Rain', 'Cool ' ,'Normal', 'Weak' ,'yes'],
            ['Rain', 'Cool ', 'Normal' ,'Strong' ,'no'],
            ['Overcast', 'Cool', 'Normal', 'Strong' ,'yes'],
            ['Overcast', 'Mild', 'High', 'Weak','no'],
            ['Sunny', 'Cool', 'Normal', 'Weak' ,'yes'],
            ['Rain', 'Mild', 'Normal' ,'Weak' ,'yes']
            ]
    
    return np.array(data)
    
train_data = create_train_data()
print(train_data)

def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))
    for i in range(len(y_unique)):
        prior_probability[i] = len(np.nonzero(train_data[:, 4] == y_unique[i])[0])/len(train_data)
    return prior_probability

prior_probability = compute_prior_probability(train_data)
print("P(play tennis = No)", prior_probability[0])
print("P(play tennis = Yes)", prior_probability[1])

def compute_conditional_probility(train_data):
    y_unique = ['no', 'yes']
    conditional_probility = []
    list_x_name = []
    for i in range(train_data.shape[1]-1):
        x_unique = np.unique(train_data[:, i])
        #print(x_unique)
        list_x_name.append(x_unique)
        
        x_conditional_probility = np.zeros((len(y_unique), len(x_unique)))
        for j in range(len(y_unique)):
            for k in range(len(x_unique)):
                x_conditional_probility[j, k] = len(np.nonzero((train_data[:, i] == x_unique[k]) & (train_data[:, 4] == y_unique[j]))[0]) / len(np.nonzero(train_data[:, 4] == y_unique[j])[0])
        conditional_probility.append(x_conditional_probility)
    return conditional_probility, list_x_name
 
conditional_probability, list_x_name = compute_conditional_probility(train_data)       

def train_naive_bayes(train_data):
    prior_probability = compute_prior_probability(train_data)
    
    conditional_probability, list_x_name = compute_conditional_probility(train_data)  
    
    return prior_probability, conditional_probability, list_x_name

print("x1 = ", list_x_name [0])
print("x2 = ", list_x_name [1])
print("x3 = ", list_x_name [2])
print("x4 = ", list_x_name [3])

def get_index(f_name, list_features):
     return np.nonzero(list_features == f_name) [0][0]
 
outlook = list_x_name[0]

i1 = get_index("Overcast", outlook )
i2 = get_index("Rain", outlook )
i3 = get_index ("Sunny", outlook )

print(i1, i2, i3)

x1 = get_index("Sunny", list_x_name[0])
print("P(’Outlook’ = ’Sunny’ | 'Play Tennis’ = ’Yes’) = ", np.round(conditional_probability[0][1, x1], 2))
print("P(’Outlook’ = ’Sunny’ | 'Play Tennis’ = ’No’) = ", np.round(conditional_probability[0][0, x1], 2))

def predict(X, list_x_name, prior_probability, conditional_probility):
    x1 = get_index(X[0], list_x_name[0])
    x2 = get_index(X[1], list_x_name[1])
    x3 = get_index(X[2], list_x_name[2])
    x4 = get_index(X[3], list_x_name[3])
    
    p0 = prior_probability[0] \
    *conditional_probility[0] [0, x1] \
    *conditional_probility[1] [0, x2] \
    *conditional_probility[2] [0, x3] \
    *conditional_probility[3] [0, x4]
    
    p1 = prior_probability[1] \
    *conditional_probility[0] [1, x1] \
    *conditional_probility[1] [1, x2] \
    *conditional_probility[2] [1, x3] \
    *conditional_probility[3] [1, x4]
    
    if p0 > p1:
        y_pred = 'no'
    else:
        y_pred = 'yes'
    return y_pred    
    
X = ['Sunny', 'Cool', 'High', 'Strong']
data = create_train_data ()
prior_probability , conditional_probability , list_x_name = train_naive_bayes(data)
pred = predict(X, list_x_name, prior_probability, conditional_probability)

if(pred):
    print("Ad should go!")
else:
    print("Ad should not go!")