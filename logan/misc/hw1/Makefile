CXXFLAGS += -g -Wall -Wextra

all : main.o utilities.o
	$(CXX) $(CXXFLAGS) $^ -o hw1

main.o : main.cpp definitions.h
	$(CXX) $(CXXFLAGS) -c main.cpp

utilities.o : utilities.cpp definitions.h
	$(CXX) $(CXXFLAGS) -c utilities.cpp

clean :
	rm -f *.o hw1

