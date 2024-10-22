import pickle
from punkt import NazwanyPunkt, Punkt


punkty = [Punkt(1, 2), NazwanyPunkt(3, 4), NazwanyPunkt(5, 6), Punkt(7, 8)]
f = open('punkty.pkl', 'wb')
pickle.dump(punkty, f)
f.close()

f = open('punkty.pkl', 'rb')
print(pickle.load(f))
f.close()
