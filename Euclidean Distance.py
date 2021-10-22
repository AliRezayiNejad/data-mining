import numpy as np
def Calculate_the_Euclidean_distance(i,j):
data1 = [df['math score'][i],df['reading score'][i],df['writing score'][i]]
data2 = [df['math score'][j],df['reading score'][j],df['writing score'][j]]
point1 = np.array((data1))
point2 = np.array((data2))
print(f'first record :{data1}')
print(f'second record :{data2}')
dist = np.linalg.norm(point1 - point2)
print(f"Euclidean distance << record {i} >> and << record {j} >> is : {dist}")
print('Records start at 0 and end at 999 ')
i=int(input('Enter first number of record : '))
j=int(input('Enter second number of record : '))
Calculate_the_Euclidean_distance(i,j)